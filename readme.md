klik kanan readme.md > open preview biar bisa baca.

# AWAL
Kalo mau jalanin kode disaranin pake venv. ga juga gapapa.
kalo mau pake venv, pas ditanya install modul apa aja klik <span style="color:teal">requirements.txt</span>. harusnya aman.
<br>
Kalo ga mau pake venv. cukup "pip install <span style="color:green">supabase</span> <span style="color:orange">flask</span>"

# TODO
* Get data spesifik "GET /products/id" dll
<br>
* Business logic kaya:
    * stok ga ada = gabisa checkout
    * ada berhasil co = kurangin stok
    * itung total price serverside
    * clear cart abis co
    * DLL.....



# DEBUG/KALO ADA ERROR
kalo data ga muncul di localhost/tabel, minta akses ke <span style="color:green">supabase</span>. dengan cara :
<br>
create policy "Allow read access to [table]"
<br>
on [table]
<br>
for select
<br>
using (true);
