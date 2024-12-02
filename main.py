import re
import sys

def informacao_relevante(log_linha):
    patterns = {
        'user': r'user="([^"]*)"',
        'hostname': r'hostname="([^"]*)"',
        'url': r'url="([^"]*)"',
        'action': r'action="([^"]*)"'
    }

    result = {}
    
    for key, pattern in patterns.items():
        match = re.search(pattern, log_linha)
        if match:
            result[key] = match.group(1)
        else:
            result[key] = 'N/A'
    
    return result

def main(input_file, output_file):
    hostname_count = {}  
    last_occurrence = {}  
    
    with open(input_file, 'r') as infile:
        for linha in infile:
            info = informacao_relevante(linha)
            hostname = info['hostname']
            
            if hostname in hostname_count:
                hostname_count[hostname] += 1
            else:
                hostname_count[hostname] = 1
                last_occurrence[hostname] = info
    
    # Ordenar os hostnames em ordem alfabética
    sorted_hostnames = sorted(hostname_count.keys())
    
    with open(output_file, 'w') as outfile:
        for hostname in sorted_hostnames:
            count = hostname_count[hostname]
            if count > 0:
                info = last_occurrence[hostname]
                formatted_linha = (f"user={info['user']} "
                                   f"hostname={hostname} action={info['action']} "
                                   f"url={info['url']} hostnamerepeat={count}\n")
                outfile.write(formatted_linha)

if __name__ == '__main__':
    # Verificar se os argumentos foram passados
    if len(sys.argv) != 3:
        print("Uso: python script.py <input_file> <output_file>")
        sys.exit(1)

    # executa os parametros de linha de comando
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    main(input_file, output_file)
