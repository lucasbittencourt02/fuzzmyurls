import subprocess
import argparse
import re

def print_banner(message):
    print("\n" + "=" * 50)
    print(f"{message}")
    print("=" * 50 + "\n")

def fuzz_url(url, palavra, output_file, hide_codes, hide_lines, hide_words, hide_headers):
    # Montar o comando com o cabeçalho User-Agent
    comando = f'wfuzz -c -z file,{palavra} -H "User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 OpenWave/93.4.3797.32" {url}/FUZZ'
    
    # Adicionando as opções de ocultação
    if hide_codes:
        comando += f' -hc {hide_codes}'
    if hide_lines:
        comando += f' -hl {hide_lines}'
    if hide_words:
        comando += f' -hw {hide_words}'
    if hide_headers:
        comando += f' -hh {hide_headers}'
    
    print(f'Executing command: {comando}')  # Linha de depuração
    result = subprocess.run(comando, shell=True, text=True, capture_output=True)
    
    if result.stdout:
        for line in result.stdout.splitlines():
            match = re.search(r'(\d{3})\s', line)
            if match:
                status_code = match.group(1)
                if status_code in {'200', '201', '301', '401', '403'}:
                    print(line)  # Imprime na saída padrão
                    with open(output_file, 'a') as f:
                        f.write(line + '\n')

def main():
    parser = argparse.ArgumentParser(description='Fuzzing em URLs')
    parser.add_argument("-u", "--urls", required=True, help="Arquivo contendo URLs")
    parser.add_argument('-w', "--wordlist-dir", required=True, help="Arquivo de palavras para fuzzing de diretórios")
    parser.add_argument('-f', "--wordlist-file", required=True, help="Arquivo de palavras para fuzzing de arquivos")
    parser.add_argument('-o', "--output", default="fuzz_results.txt", help="Arquivo para armazenar resultados (padrão: fuzz_results.txt)")
    parser.add_argument('--hide-codes', help="Códigos de status a serem ocultados (separados por vírgula)")
    parser.add_argument('--hide-lines', help="Linhas a serem ocultadas (separadas por vírgula)")
    parser.add_argument('--hide-words', help="Palavras a serem ocultadas (separadas por vírgula)")
    parser.add_argument('--hide-headers', help="Cabeçalhos a serem ocultados (separados por vírgula)")
    
    args = parser.parse_args()

    # Verificar se os arquivos existem
    for arg in [args.urls, args.wordlist_dir, args.wordlist_file]:
        try:
            with open(arg, 'r'):
                pass
        except FileNotFoundError:
            print(f"Erro: O arquivo {arg} não foi encontrado.")
            return

    # Lê as URLs do arquivo
    with open(args.urls, 'r') as f:
        urls = f.readlines()

    urls = [url.strip() for url in urls]

    # Fuzzing de diretórios
    print_banner("Iniciando Fuzzing de Diretórios")
    for url in urls:
        if url:
            print(f"Fuzzing de diretórios para: {url}")  # Linha de depuração
            fuzz_url(url, args.wordlist_dir, args.output, args.hide_codes, args.hide_lines, args.hide_words, args.hide_headers)

    # Fuzzing de arquivos
    print_banner("Iniciando Fuzzing de Arquivos")
    for url in urls:
        if url:
            print(f"Fuzzing de arquivos para: {url}")  # Linha de depuração
            fuzz_url(url, args.wordlist_file, args.output, args.hide_codes, args.hide_lines, args.hide_words, args.hide_headers)

if __name__ == '__main__':
    main()
