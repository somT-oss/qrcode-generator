from django.db import models
import qrcode
from PIL import Image, ImageDraw
from django.core.files import File
from io import BytesIO


class UserQrcode(models.Model):

    username = models.CharField(max_length=255)
    parent_email = models.EmailField(max_length=245)
    qrcode = models.ImageField(upload_to='qrcodes', blank=True)

    def save(self, *args, **kwargs):
        qrcode_img = qrcode.make(self.username)
        canvas = Image.new('RGB', (290, 290), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        frame = f'{self.username} qrcode.png'
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        self.qrcode.save(frame, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"This qrcode belongs to {self.username}"
