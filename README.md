## school_system_API

- This project internally uses AWS S3 bucket to store images, videos, files and django admin static files

- If you clone this project make sure you entered following key values 

- DEFAULT_FILE_STORAGE=""

- STATICFILES_STORAGE = ""

- AWS_ACCESS_KEY_ID=""

- AWS_SECRET_ACCESS_KEY=""

- AWS_STORAGE_BUCKET_NAME=""

No only these filed ..optional fields can be added

- To Get full details click below link

```
https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html
```

Last but not least, You should add CORS to your bucket to get out of mysterious problems.
```
<?xml version="1.0" encoding="UTF-8"?>
<CORSConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
   <CORSRule>
        <AllowedOrigin>*</AllowedOrigin>
        <AllowedMethod>GET</AllowedMethod>
        <AllowedMethod>POST</AllowedMethod>
        <AllowedMethod>PUT</AllowedMethod>
        <AllowedHeader>*</AllowedHeader>
    </CORSRule>
</CORSConfiguration>
```

Add this code and save.
