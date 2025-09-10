import os
from supabase import create_client, Client

url= "https://gnhgcpdfnrrepdlarjuh.supabase.co"
key= "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImduaGdjcGRmbnJyZXBkbGFyanVoIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTczMTUyMDYsImV4cCI6MjA3Mjg5MTIwNn0.wbcp3WLpeVeMHC1iSoLeQY9ZrgdNXY-cbv4PF1ZdMRA"
supabase= create_client(url, key)

response = supabase.table('products').select('*').execute()
print(response) # -> ini buat ngetes koneksinya udah jalan atau belom