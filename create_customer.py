import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()

from pagination.models import Customer

Customer.objects.create(name = "Tuong An", country = "Vietnam")
Customer.objects.create(name = "Kiki Xu", country = "China")
Customer.objects.create(name = "Hei Qi Jun", country = "China")
Customer.objects.create(name = "Fair Xing", country = "China")
Customer.objects.create(name = "Doraemon", country = "Japan")
Customer.objects.create(name = "Conan", country = "Japan")
Customer.objects.create(name = "Park Shin Hye", country = "Korea")
Customer.objects.create(name = "Lee Jong Suk", country = "Korea")
Customer.objects.create(name = "Kim Young Dae", country = "Korea")
Customer.objects.create(name = "Lee Min Ho", country = "Korea")
Customer.objects.create(name = "Ji Chang Wook", country = "Korea")
Customer.objects.create(name = "Lin Yi", country = "China")
Customer.objects.create(name = "Hu Yi Tian", country = "China")
Customer.objects.create(name = "Song Wei Long", country = "China")
Customer.objects.create(name = "Yu Shu Xin", country = "China")
Customer.objects.create(name = "Dai Meng", country = "China")
Customer.objects.create(name = "Lisa", country = "Thailand")
Customer.objects.create(name = "Kang Daniel", country = "Korea")
Customer.objects.create(name = "Bae Suzy", country = "Korea")
Customer.objects.create(name = "Nguyen Thi My Huong", country = "Vietnam")
Customer.objects.create(name = "Steve Carbon", country = "USA")
Customer.objects.create(name = "An Qi", country = "China")
Customer.objects.create(name = "Bam Bam", country = "Thailand")
Customer.objects.create(name = "Seo In Ah", country = "Korea")
Customer.objects.create(name = "Han Soo Hee", country = "Korea")
Customer.objects.create(name = "Lee Ho Jung", country = "Korea")
Customer.objects.create(name = "Snow Kong", country = "China")
Customer.objects.create(name = "Liu Yu Xin", country = "China")
Customer.objects.create(name = "Yu Yan", country = "China")