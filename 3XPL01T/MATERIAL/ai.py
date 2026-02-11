import sys

def compare_files(file1, file2, output_file):
    # Baca isi file
    with open(file1, 'r', encoding='utf-8') as f1:
        text1 = f1.read().lower().split()
    with open(file2, 'r', encoding='utf-8') as f2:
        text2 = f2.read().lower().split()

    # Ubah ke set
    set1 = set(text1)
    set2 = set(text2)

    # Cari kata yang berbeda
    unique_to_file1 = set1 - set2
    unique_to_file2 = set2 - set1

    # Gabungkan semua perbedaan
    all_differences = unique_to_file1.union(unique_to_file2)

    # Simpan hasil ke file output
    with open(output_file, 'w', encoding='utf-8') as out:
        if all_differences:
            out.write("\n".join(sorted(all_differences)))
        else:
            out.write("Tidak ada perbedaan kata.\n")

    print(f"Hasil perbandingan disimpan di '{output_file}'")
    print(f"Total kata berbeda: {len(all_differences)}")

if __name__ == "__main__":
    # Pastikan argumen cukup
    if len(sys.argv) != 4:
        print("Cara pakai:")
        print("python3 compare_ai.py file1.txt file2.txt resulttidaksama.txt")
        sys.exit(1)

    file1 = sys.argv[1]
    file2 = sys.argv[2]
    output = sys.argv[3]

    compare_files(file1, file2, output)
