from urllib.parse import urlparse

def extract_domain(url):
    """Mengambil domain dari URL untuk perbandingan."""
    parsed_url = urlparse(url)
    return parsed_url.netloc  # Mengambil bagian domain dari URL

def find_common_lines(file1, file2, output_file):
    try:
        # Membaca isi file list1.txt dan list2.txt
        with open(file1, 'r') as f1, open(file2, 'r') as f2:
            # Menghapus karakter newline dan spasi ekstra pada setiap baris
            lines1 = [line.strip() for line in f1.readlines()]
            lines2 = [line.strip() for line in f2.readlines()]

        # Menyaring domain dari URL di kedua file
        domains1 = set(extract_domain(line) for line in lines1)
        domains2 = set(extract_domain(line) for line in lines2)

        # Mencari irisan (kesamaan) antara domain di kedua file
        common_domains = domains1.intersection(domains2)

        # Menyaring baris asli yang memiliki domain yang sama
        common_lines = set()  # Menggunakan set untuk menghilangkan duplikat

        # Menambahkan baris yang memiliki domain yang sama dari file pertama
        for line in lines1:
            if extract_domain(line) in common_domains:
                common_lines.add(line)

        # Menambahkan baris yang memiliki domain yang sama dari file kedua
        for line in lines2:
            if extract_domain(line) in common_domains:
                common_lines.add(line)

        # Jika ada hasil, menulis ke dalam output.txt
        if common_lines:
            # Mengurutkan hasil secara alfabetis
            sorted_common_lines = sorted(common_lines)

            # Menulis hasil yang terurut ke dalam file output
            with open(output_file, 'w') as result_file:
                result_file.writelines(f"{line}\n" for line in sorted_common_lines)
            print(f"Common lines have been written to {output_file}")
        else:
            print("No common lines found between the files.")

    except Exception as e:
        print(f"An error occurred: {e}")

# Memastikan program berjalan dengan argumen yang sesuai
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        print("Usage: python3 check.py <list1.txt> <list2.txt> <results.txt>")
    else:
        list1_file = sys.argv[1]
        list2_file = sys.argv[2]
        results_file = sys.argv[3]

        find_common_lines(list1_file, list2_file, results_file)
