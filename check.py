content = open('index.html', encoding='utf-8').read()
items = [
    ('public/profile.png', 'portrait src'),
    ('portrait-mask', 'portrait mask class'),
    ('portrait-rim', 'portrait rim class'),
    ('portrait-enter', 'portrait animation'),
    ('watermark-enter', 'watermark animation'),
    ('ABHINAVKRISHNAN M', 'full name'),
    ('Open to work', 'open to work chip'),
    ('mousemove', 'parallax JS'),
    ('lucide.createIcons', 'lucide init'),
    ('bankingGallery', 'banking modal'),
    ('id="projects"', 'projects section'),
    ('id="skills"', 'skills section'),
    ('id="contact"', 'contact section'),
    ('.portrait-mask', 'portrait-mask CSS'),
    ('.portrait-rim', 'portrait-rim CSS'),
    ('.film-grain', 'film-grain CSS'),
]
all_ok = True
for pat, name in items:
    if pat not in content:
        print('MISSING:', name, '->', pat)
        all_ok = False
if all_ok:
    print('ALL CHECKS PASSED!')
print('Total lines:', content.count('\n'))
