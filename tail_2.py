import sys
import linecache

# fungsi akan menampilan error jika argumennya kurang
if len(sys.argv) !=3:
    # sistem akan mencetak pesan ini
    print ('Usage: tail_2.py <file> <nlines>')
    # fungsi sys exit untuk membatalkan eksekusi program saat ini
    sys.exit(1)

# variabel nama file dan nomor line yang diminta di sys argv 1 
fname, nlines = sys.argv[1:]
nlines = int(nlines)
# fungsi agar default bernilai 10 
if (nlines < 10):
    nlines = 10
# menghitung ada beberapa baris dari file
tbaris = len(open(fname).readlines())
# fungsi untuk menentukan loopnya
for i in range(tbaris - nlines + 1, tbaris+1):
    # mencetak menggunakan modul linecache untuk membaca baris 
    print (linecache.getline(sys.argv[1],i))