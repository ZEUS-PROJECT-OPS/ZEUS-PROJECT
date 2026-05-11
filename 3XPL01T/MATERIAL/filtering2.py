#!/usr/bin/env python3
# @author General Zeus OPS with FBI NCA INTERPOL BARESKRIM POLRI

def nomi_filter():
    
    print("""
   ╔═══════════════════════════════════════════════════════════════╗
   ║      ███████╗███████╗██╗   ██╗███████╗                       ║
   ║      ╚══███╔╝██╔════╝██║   ██║██╔════╝                       ║
   ║        ███╔╝ █████╗  ██║   ██║███████╗                       ║
   ║       ███╔╝  ██╔══╝  ██║   ██║╚════██║                       ║
   ║      ███████╗███████╗╚██████╔╝███████║                       ║
   ║      ╚══════╝╚══════╝ ╚═════╝ ╚══════╝                       ║
   ║                                                               ║
   ║   ╔═══════════════════════════════════════════════════════╗   ║
   ║   ║     🔥 DOMAIN FILTER TOOL  |  ZEUS-PROJECT-OPS        ║   ║
   ║   ╚═══════════════════════════════════════════════════════╝   ║
   ╚═══════════════════════════════════════════════════════════════╝
    """)
    
    print("\033[93m[+] ZEUS DOMAIN FILTER LOADED\033[0m\n")
    
    
    extensions_input = input("\033[96m[?] Extension: \033[0m")
    allowed_domains = set()
    
    for ext in extensions_input.split(','):
        ext = ext.strip().lower()
        if not ext.startswith('.'):
            ext = '.' + ext
        allowed_domains.add(ext)
    
    
    input_file = input("\033[96m[?] Input file: \033[0m")
    output_file = input("\033[96m[?] Output file: \033[0m")
    
    
    raw_domains = set()
    total_lines = 0
    
    print("\n\033[93m[*] Processing...\033[0m")
    
    try:
        
        with open(input_file, 'r', encoding='utf-8') as f:
            total_lines = sum(1 for _ in f)
        
        
        with open(input_file, 'r', encoding='utf-8') as f:
            for idx, line in enumerate(f, 1):
                line = line.strip().lower()
                if not line:
                    continue
                    
                
                if idx % 1000 == 0 or idx == total_lines:
                    print(f"\r\033[90m[>] Progress: {idx}/{total_lines} lines\033[0m", end='', flush=True)
                
                
                for ext in allowed_domains:
                    if line.endswith(ext):
                        raw_domains.add(line)
                        break
        
        print()  
        
        
        with open(output_file, 'w', encoding='utf-8') as f:
            for domain in sorted(raw_domains):
                f.write(domain + '\n')
        
        
        print(f"\n\033[92m[✓] DONE!\033[0m")
        print(f"\033[92m[✓] Total unique domains: {len(raw_domains)}\033[0m")
        print(f"\033[92m[✓] Saved to: {output_file}\033[0m")
        
    except FileNotFoundError:
        print(f"\n\033[91m[✗] ERROR: File '{input_file}' not found!\033[0m")
    except Exception as e:
        print(f"\n\033[91m[✗] ERROR: {str(e)}\033[0m")

if __name__ == "__main__":
    nomi_filter()