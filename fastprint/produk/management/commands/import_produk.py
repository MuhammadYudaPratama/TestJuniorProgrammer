from django.core.management.base import BaseCommand
import requests, hashlib
from datetime import datetime
from produk.models import Produk, Kategori, Status


class Command(BaseCommand):
    help = "Import produk dari API Fastprint"

    def handle(self, *args, **kwargs):
        url = "https://recruitment.fastprint.co.id/tes/api_tes_programmer"

        # Username dari soal (bersifat dinamis)
        username = "tesprogrammer010226C11"

        # Password format + MD5
        today = datetime.now()
        raw_password = f"bisacoding-{today.day}-{today.month}-{str(today.year)[-2:]}"
        password = hashlib.md5(raw_password.encode()).hexdigest()

        session = requests.Session()

        payload = {
            "username": username,
            "password": password
        }

        response = session.post(url, data=payload)

        try:
            result = response.json()
        except Exception:
            self.stdout.write(self.style.ERROR("Response API bukan JSON"))
            return

        # ======================================================
        # JIKA API GAGAL (USERNAME EXPIRED / TIDAK VALID)
        # ======================================================
        if result.get("error") == 1:
            self.stdout.write(self.style.WARNING(
                "API tidak dapat diakses, menggunakan dummy data"
            ))
            self.stdout.write(str(result))

            dummy_data = [
                {
                    "nama_produk": "Printer Epson L3110",
                    "harga": 2500000,
                    "kategori": "Elektronik",
                    "status": "bisa dijual"
                },
                {
                    "nama_produk": "Tinta Printer Original",
                    "harga": 150000,
                    "kategori": "Aksesoris",
                    "status": "tidak bisa dijual"
                }
            ]

            for item in dummy_data:
                kategori, _ = Kategori.objects.get_or_create(
                    nama_kategori=item["kategori"]
                )
                status, _ = Status.objects.get_or_create(
                    nama_status=item["status"]
                )
                Produk.objects.get_or_create(
                    nama_produk=item["nama_produk"],
                    harga=item["harga"],
                    kategori=kategori,
                    status=status
                )

            self.stdout.write(self.style.SUCCESS(
                "Dummy data berhasil disimpan"
            ))
            return

        # ======================================================
        # JIKA API BERHASIL
        # ======================================================
        for item in result["data"]:
            kategori, _ = Kategori.objects.get_or_create(
                nama_kategori=item["kategori"]
            )
            status, _ = Status.objects.get_or_create(
                nama_status=item["status"]
            )
            Produk.objects.get_or_create(
                nama_produk=item["nama_produk"],
                harga=item["harga"],
                kategori=kategori,
                status=status
            )

        self.stdout.write(self.style.SUCCESS(
            "Import produk dari API berhasil"
        ))
