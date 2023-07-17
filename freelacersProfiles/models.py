from django.db import models


class Freelancer(models.Model):
    LANGUAGE_CHOICES = [
        ('front_end', 'Front_end Developer'),
        ('back_end', 'Back_end Developer'),
        ('full stack', 'Full Stack Developer'),
        ('gaming', 'Gaming Developer'),
        ('android', 'Android Developer'),
        ('ios', 'IOS Developer'),
        ('software', 'software Developer'),
        ('software', 'software Engineer'),
        ('qa', 'QA'),
        ('penetration testing', 'Penetration Testing'),
        ('typer', 'Typer'),
        ('translator', 'Translator'),
        ('it', 'IT'),
        ('devops', 'DevOps'),
        ('ux/ui', 'UX/UI'),
        ('web designer', 'Web Designer'),
        ('seo', 'SEO'),
        ('aso', 'ASO'),
        ('graphic designer', 'Graphic Designer'),
    ]

    cover_img = models.ImageField(null=True, blank=True, upload_to='images/')
    profession = models.CharField(max_length=20, choices=LANGUAGE_CHOICES)
    name = models.CharField('Name', max_length=50)
    last_name = models.CharField('Last_name', max_length=50)
    experience = models.CharField('Experience', max_length=50)
    skills = models.TextField('skills')
    cover_letter = models.TextField('Cover_Letter')



    def __str__(self):
        return self.profession
