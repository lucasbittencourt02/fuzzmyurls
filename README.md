# fuzzmyurls

Fuzzing multiples URLS  using Wfuzz and Python

This is a simple tool automation to Bug Bounty Programs.

```

python3 fuzzmyurls.py --help
usage: fuzzmyurls.py [-h] -u URLS -w WORDLIST_DIR
                     -f WORDLIST_FILE [-o OUTPUT]
                     [--hide-codes HIDE_CODES]
                     [--hide-lines HIDE_LINES]
                     [--hide-words HIDE_WORDS]
                     [--hide-headers HIDE_HEADERS]

Fuzzing em URLs

options:
  -h, --help            show this help message
                        and exit
  -u URLS, --urls URLS  Arquivo contendo URLs
  -w WORDLIST_DIR, --wordlist-dir WORDLIST_DIR
                        Arquivo de palavras para
                        fuzzing de diretórios
  -f WORDLIST_FILE, --wordlist-file WORDLIST_FILE
                        Arquivo de palavras para
                        fuzzing de arquivos
  -o OUTPUT, --output OUTPUT
                        Arquivo para armazenar
                        resultados (padrão:
                        fuzz_results.txt)
  --hide-codes HIDE_CODES
                        Códigos de status a serem
                        ocultados (separados por
                        vírgula)
  --hide-lines HIDE_LINES
                        Linhas a serem ocultadas
                        (separadas por vírgula)
  --hide-words HIDE_WORDS
                        Palavras a serem
                        ocultadas (separadas por
                        vírgula)
  --hide-headers HIDE_HEADERS
                        Cabeçalhos a serem
                        ocultados (separados por
                        vírgula)
```