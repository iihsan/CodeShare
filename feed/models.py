from django.db import models
from django.contrib.auth.models import User
from users.models import Profile
from django.urls import reverse
from django.utils import timezone

# This model is for any post that a user posts on the website.
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=255, blank=True)
    code = models.TextField(blank=True, null=True)
    langs = [('text', 'None'),
            ('Markup', 'markup'),
            ('html', 'html'),
             ('CSS', 'css'),
             ('C-like', 'clike'),
             ('JavaScript', 'javascript, js'),
             ('Arduino', 'arduino'),
             ('Bash', 'bash, shell'),
             ('BASIC', 'basic'),
             ('C', 'c'),
             ('C#', 'csharp, cs, dotnet'),
             ('Cpp', 'cpp'),
             ('CoffeeScript', 'coffeescript, coffee'),
             ('CMake', 'cmake'),
             ('Clojure', 'clojure'),
             ('Django/Jinja2', 'django, jinja2'),
             ('Docker', 'docker, dockerfile'),
             ('Git', 'git'),
             ('GameMaker Language', 'gml, gamemakerlanguage'),
             ('Go', 'go'),
             ('GraphQL', 'graphql'),
             ('Groovy', 'groovy'),
             ('Haml', 'haml'),
             ('HTTP', 'http'),
             ('Icon', 'icon'),
             ('Java', 'java'),
             ('JavaDoc', 'javadoc'),
             ('JSDoc', 'jsdoc'),
             ('JSON', 'json'),
             ('JSONP', 'jsonp'),
             ('JSON5', 'json5'),
             ('Kotlin', 'kotlin'),
             ('LaTeX', 'latex, tex, context'),
             ('Latte', 'latte'),
             ('Less', 'less'),
             ('LiveScript', 'livescript'),
             ('Lua', 'lua'),
             ('Makefile', 'makefile'),
             ('Markdown', 'markdown, md'),
             ('MATLAB', 'matlab'),
             ('nginx', 'nginx'),
             ('Objective-C', 'objectivec'),
             ('OpenCL', 'opencl'),
             ('Parser', 'parser'),
             ('Pascal', 'pascal, objectpascal'),
             ('Perl', 'perl'),
             ('PHP', 'php'),
             ('PL/SQL', 'plsql'),
             ('PowerShell', 'powershell'),
             ('Pug', 'pug'),
             ('Python', 'python, py'),
             ('R', 'r'),
             ('React JSX', 'jsx'),
             ('React TSX', 'tsx'),
             ('Regex', 'regex'),
             ('Ruby', 'ruby, rb'),
             ('Rust', 'rust'),
             ('SAS', 'sas'),
             ('Sass (Sass)', 'sass'),
             ('Sass (Scss)', 'scss'),
             ('Scala', 'scala'),
             ('SQL', 'sql'),
             ('Stylus', 'stylus'),
             ('Swift', 'swift'),
             ('Twig', 'twig'),
             ('TypeScript', 'typescript, ts'),
             ('Velocity', 'velocity'),
             ('vim', 'vim'),
             ('Visual Basic', 'visual-basic, vb'),
             ('Wiki markup', 'wiki'),
             ('YAML', 'yaml, yml'),
             ('Zig', 'zig'),

             ]
    lang = models.CharField(max_length=18, choices=langs, default='text')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.CharField(max_length=100, blank=True)
    posted_on = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
	
 
# Comment model links a comment with the post and the user. 
class Comments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    comment = models.CharField(max_length=255)
    commented_on = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.comment + " => " + self.post.title
    

# It stores the like info. It has the user who created the like and the post on which like was made.
class Like(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)	
