import requests
import traceback
import random
import string
import ast
import os
from PIL import Image
from PIL import ImageFile, ImageFilter
ImageFile.LOAD_TRUNCATED_IMAGES = True


def rape(message):
    if message.attachments != []:
        url = ast.literal_eval(str(message.attachments).split("[")[1].split("]")[0])
        if url['filename'].lower().endswith('png') or url['filename'].lower().endswith('jpg') or url['filename'].lower().endswith('jpeg') or url['filename'].lower().endswith('bmp'):
            r = requests.get(url['url'], stream=True)
            if r.status_code == 200:
                with open(''.join(('tmp/', url['filename'])), 'wb') as f:
                    for chunk in r:
                        f.write(chunk)

                filepath = ''.join(('tmp/', str(url['filename'])))
                try:
                    picture = Image.open(filepath)
                except:
                    traceback.print_exc()
                    return True, 3, ''
                rand_discriminator = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(5))
                localfile = '/discordcdn/rape/' + message.channel.id + '/' + message.author.id + '/' + url['filename'] + str(rand_discriminator) + '.jpg'
                if not os.path.exists('/discordcdn/rape/' + message.channel.id):
                    os.makedirs('/discordcdn/rape/' + message.channel.id)
                if not os.path.exists('/discordcdn/rape/' + message.channel.id + '/' + message.author.id):
                    os.makedirs('/discordcdn/rape/' + message.channel.id + '/' + message.author.id)
                try:
                    picture = picture.convert('RGB')
                    picture = picture.filter(ImageFilter.UnsharpMask(80000,80000,0))
                    picture.save(localfile,"JPEG",optimize=False,quality=1)
                    remotefile = 'http://cdn.jplp.tk/rape/' + message.channel.id + '/' + message.author.id + '/' + url['filename'] + str(rand_discriminator) + '.jpg'
                except:
                    traceback.print_exc()
                    return True, 4, ''

                return False, 0, remotefile
            else:
                return True, 2, ''
        else:
            if message.mentions == []:
                r = requests.get(message.author.avatar_url, stream=True)
                if r.status_code == 200:
                    with open(''.join(('tmp/', message.author.avatar_url.split('/')[-1].split('?')[0])), 'wb') as f:
                        for chunk in r:
                            f.write(chunk)

                    filepath = ''.join(('tmp/', message.author.avatar_url.split('/')[-1].split('?')[0]))
                    try:
                        picture = Image.open(filepath)
                    except:
                        traceback.print_exc()
                        return True, 3, ''
                    rand_discriminator = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(5))
                    localfile = '/discordcdn/rape/' + message.channel.id + '/' + message.author.id + '/' + message.author.avatar_url.split('/')[-1].split('?')[0] + str(rand_discriminator) + '.jpg'
                    if not os.path.exists('/discordcdn/rape/' + message.channel.id):
                        os.makedirs('/discordcdn/rape/' + message.channel.id)
                    if not os.path.exists('/discordcdn/rape/' + message.channel.id + '/' + message.author.id):
                        os.makedirs('/discordcdn/rape/' + message.channel.id + '/' + message.author.id)
                    try:
                        picture = picture.convert('RGB')
                        #picture = picture.filter(ImageFilter.UnsharpMask(80000,80000,0))
                        picture.save(localfile,"JPEG",optimize=False,quality=1)
                        remotefile = 'http://cdn.jplp.tk/rape/' + message.channel.id + '/' + message.author.id + '/' + message.author.avatar_url.split('/')[-1].split('?')[0] + str(rand_discriminator) + '.jpg'
                    except:
                        traceback.print_exc()
                        return True, 4, ''

                    return False, 0, remotefile
            else:
                r = requests.get(message.mentions[0].avatar_url, stream=True)
                if r.status_code == 200:
                    with open(''.join(('tmp/', message.mentions[0].avatar_url.split('/')[-1].split('?')[0])), 'wb') as f:
                        for chunk in r:
                            f.write(chunk)

                    filepath = ''.join(('tmp/', message.mentions[0].avatar_url.split('/')[-1].split('?')[0]))
                    try:
                        picture = Image.open(filepath)
                    except:
                        traceback.print_exc()
                        return True, 3, ''
                    rand_discriminator = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(5))
                    localfile = '/discordcdn/rape/' + message.channel.id + '/' + message.author.id + '/' + message.mentions[0].avatar_url.split('/')[-1].split('?')[0] + str(rand_discriminator) + '.jpg'
                    if not os.path.exists('/discordcdn/rape/' + message.channel.id):
                        os.makedirs('/discordcdn/rape/' + message.channel.id)
                    if not os.path.exists('/discordcdn/rape/' + message.channel.id + '/' + message.author.id):
                        os.makedirs('/discordcdn/rape/' + message.channel.id + '/' + message.author.id)
                    try:
                        picture = picture.convert('RGB')
                        #picture = picture.filter(ImageFilter.UnsharpMask(80000,80000,0))
                        picture.save(localfile,"JPEG",optimize=False,quality=1)
                        remotefile = 'http://cdn.jplp.tk/rape/' + message.channel.id + '/' + message.author.id + '/' + message.mentions[0].avatar_url.split('/')[-1].split('?')[0] + str(rand_discriminator) + '.jpg'
                    except:
                        traceback.print_exc()
                        return True, 4, ''

                    return False, 0, remotefile
    else:
        if message.mentions == []:
            r = requests.get(message.author.avatar_url, stream=True)
            if r.status_code == 200:
                with open(''.join(('tmp/', message.author.avatar_url.split('/')[-1].split('?')[0])), 'wb') as f:
                    for chunk in r:
                        f.write(chunk)

                filepath = ''.join(('tmp/', message.author.avatar_url.split('/')[-1].split('?')[0]))
                try:
                    picture = Image.open(filepath)
                except:
                    traceback.print_exc()
                    return True, 3, ''
                rand_discriminator = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(5))
                localfile = '/discordcdn/rape/' + message.channel.id + '/' + message.author.id + '/' + message.author.avatar_url.split('/')[-1].split('?')[0] + str(rand_discriminator) + '.jpg'
                if not os.path.exists('/discordcdn/rape/' + message.channel.id):
                    os.makedirs('/discordcdn/rape/' + message.channel.id)
                if not os.path.exists('/discordcdn/rape/' + message.channel.id + '/' + message.author.id):
                    os.makedirs('/discordcdn/rape/' + message.channel.id + '/' + message.author.id)
                try:
                    picture = picture.convert('RGB')
                    #picture = picture.filter(ImageFilter.UnsharpMask(80000,80000,0))
                    picture.save(localfile,"JPEG",optimize=False,quality=1)
                    remotefile = 'http://cdn.jplp.tk/rape/' + message.channel.id + '/' + message.author.id + '/' + message.author.avatar_url.split('/')[-1].split('?')[0] + str(rand_discriminator) + '.jpg'
                except:
                    traceback.print_exc()
                    return True, 4, ''

                return False, 0, remotefile
        else:
            r = requests.get(message.mentions[0].avatar_url, stream=True)
            if r.status_code == 200:
                with open(''.join(('tmp/', message.mentions[0].avatar_url.split('/')[-1].split('?')[0])), 'wb') as f:
                    for chunk in r:
                        f.write(chunk)

                filepath = ''.join(('tmp/', message.mentions[0].avatar_url.split('/')[-1].split('?')[0]))
                try:
                    picture = Image.open(filepath)
                except:
                    traceback.print_exc()
                    return True, 3, ''
                rand_discriminator = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(5))
                localfile = '/discordcdn/rape/' + message.channel.id + '/' + message.author.id + '/' + message.mentions[0].avatar_url.split('/')[-1].split('?')[0] + str(rand_discriminator) + '.jpg'
                if not os.path.exists('/discordcdn/rape/' + message.channel.id):
                    os.makedirs('/discordcdn/rape/' + message.channel.id)
                if not os.path.exists('/discordcdn/rape/' + message.channel.id + '/' + message.author.id):
                    os.makedirs('/discordcdn/rape/' + message.channel.id + '/' + message.author.id)
                try:
                    picture = picture.convert('RGB')
                    #picture = picture.filter(ImageFilter.UnsharpMask(80000,80000,0))
                    picture.save(localfile,"JPEG",optimize=False,quality=1)
                    remotefile = 'http://cdn.jplp.tk/rape/' + message.channel.id + '/' + message.author.id + '/' + message.mentions[0].avatar_url.split('/')[-1].split('?')[0] + str(rand_discriminator) + '.jpg'
                except:
                    traceback.print_exc()
                    return True, 4, ''

                return False, 0, remotefile

def jpeg(message):
    if message.attachments != []:
        url = ast.literal_eval(str(message.attachments).split("[")[1].split("]")[0])
        if url['filename'].lower().endswith('png') or url['filename'].lower().endswith('jpg') or url['filename'].lower().endswith('jpeg') or url['filename'].lower().endswith('bmp'):
            r = requests.get(url['url'], stream=True)
            if r.status_code == 200:
                with open(''.join(('tmp/', url['filename'])), 'wb') as f:
                    for chunk in r:
                        f.write(chunk)

                filepath = ''.join(('tmp/', str(url['filename'])))
                try:
                    picture = Image.open(filepath)
                except:
                    traceback.print_exc()
                    return True, 3, ''
                rand_discriminator = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(5))
                localfile = '/discordcdn/jpeg/' + message.channel.id + '/' + message.author.id + '/' + url['filename'] + str(rand_discriminator) + '.jpg'
                if not os.path.exists('/discordcdn/jpeg/' + message.channel.id):
                    os.makedirs('/discordcdn/jpeg/' + message.channel.id)
                if not os.path.exists('/discordcdn/jpeg/' + message.channel.id + '/' + message.author.id):
                    os.makedirs('/discordcdn/jpeg/' + message.channel.id + '/' + message.author.id)
                try:
                    picture = picture.convert('RGB')
                    #picture = picture.filter(ImageFilter.UnsharpMask(80000,80000,0))
                    picture.save(localfile,"JPEG",optimize=False,quality=1)
                    remotefile = 'http://cdn.jplp.tk/jpeg/' + message.channel.id + '/' + message.author.id + '/' + url['filename'] + str(rand_discriminator) + '.jpg'
                except:
                    traceback.print_exc()
                    return True, 4, ''

                return False, 0, remotefile
            else:
                return True, 2, ''
        else:
            if message.mentions == []:
                r = requests.get(message.author.avatar_url, stream=True)
                if r.status_code == 200:
                    with open(''.join(('tmp/', message.author.avatar_url.split('/')[-1].split('?')[0])), 'wb') as f:
                        for chunk in r:
                            f.write(chunk)

                    filepath = ''.join(('tmp/', message.author.avatar_url.split('/')[-1].split('?')[0]))
                    try:
                        picture = Image.open(filepath)
                    except:
                        traceback.print_exc()
                        return True, 3, ''
                    rand_discriminator = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(5))
                    localfile = '/discordcdn/jpeg/' + message.channel.id + '/' + message.author.id + '/' + message.author.avatar_url.split('/')[-1].split('?')[0] + str(rand_discriminator) + '.jpg'
                    if not os.path.exists('/discordcdn/jpeg/' + message.channel.id):
                        os.makedirs('/discordcdn/jpeg/' + message.channel.id)
                    if not os.path.exists('/discordcdn/jpeg/' + message.channel.id + '/' + message.author.id):
                        os.makedirs('/discordcdn/jpeg/' + message.channel.id + '/' + message.author.id)
                    try:
                        picture = picture.convert('RGB')
                        #picture = picture.filter(ImageFilter.UnsharpMask(80000,80000,0))
                        picture.save(localfile,"JPEG",optimize=False,quality=1)
                        remotefile = 'http://cdn.jplp.tk/jpeg/' + message.channel.id + '/' + message.author.id + '/' + message.author.avatar_url.split('/')[-1].split('?')[0] + str(rand_discriminator) + '.jpg'
                    except:
                        traceback.print_exc()
                        return True, 4, ''

                    return False, 0, remotefile
            else:
                r = requests.get(message.mentions[0].avatar_url, stream=True)
                if r.status_code == 200:
                    with open(''.join(('tmp/', message.mentions[0].avatar_url.split('/')[-1].split('?')[0])), 'wb') as f:
                        for chunk in r:
                            f.write(chunk)

                    filepath = ''.join(('tmp/', message.mentions[0].avatar_url.split('/')[-1].split('?')[0]))
                    try:
                        picture = Image.open(filepath)
                    except:
                        traceback.print_exc()
                        return True, 3, ''
                    rand_discriminator = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(5))
                    localfile = '/discordcdn/jpeg/' + message.channel.id + '/' + message.author.id + '/' + message.mentions[0].avatar_url.split('/')[-1].split('?')[0].split('? + str(rand_discriminator) + '.jpg'
                    if not os.path.exists('/discordcdn/jpeg/' + message.channel.id):
                        os.makedirs('/discordcdn/jpeg/' + message.channel.id)
                    if not os.path.exists('/discordcdn/jpeg/' + message.channel.id + '/' + message.author.id):
                        os.makedirs('/discordcdn/jpeg/' + message.channel.id + '/' + message.author.id)
                    try:
                        picture = picture.convert('RGB')
                        #picture = picture.filter(ImageFilter.UnsharpMask(80000,80000,0))
                        picture.save(localfile,"JPEG",optimize=False,quality=1)
                        remotefile = 'http://cdn.jplp.tk/jpeg/' + message.channel.id + '/' + message.author.id + '/' + message.mentions[0].avatar_url.split('/')[-1].split('?')[0] + str(rand_discriminator) + '.jpg'
                    except:
                        traceback.print_exc()
                        return True, 4, ''

                    return False, 0, remotefile
    else:
        if message.mentions == []:
            r = requests.get(message.author.avatar_url, stream=True)
            if r.status_code == 200:
                with open(''.join(('tmp/', message.author.avatar_url.split('/')[-1].split('?')[0])), 'wb') as f:
                    for chunk in r:
                        f.write(chunk)

                filepath = ''.join(('tmp/', message.author.avatar_url.split('/')[-1].split('?')[0]))
                try:
                    picture = Image.open(filepath)
                except:
                    traceback.print_exc()
                    return True, 3, ''
                rand_discriminator = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(5))
                localfile = '/discordcdn/jpeg/' + message.channel.id + '/' + message.author.id + '/' + message.author.avatar_url.split('/')[-1].split('?')[0] + str(rand_discriminator) + '.jpg'
                if not os.path.exists('/discordcdn/jpeg/' + message.channel.id):
                    os.makedirs('/discordcdn/jpeg/' + message.channel.id)
                if not os.path.exists('/discordcdn/jpeg/' + message.channel.id + '/' + message.author.id):
                    os.makedirs('/discordcdn/jpeg/' + message.channel.id + '/' + message.author.id)
                try:
                    picture = picture.convert('RGB')
                    #picture = picture.filter(ImageFilter.UnsharpMask(80000,80000,0))
                    picture.save(localfile,"JPEG",optimize=False,quality=1)
                    remotefile = 'http://cdn.jplp.tk/jpeg/' + message.channel.id + '/' + message.author.id + '/' + message.author.avatar_url.split('/')[-1].split('?')[0] + str(rand_discriminator) + '.jpg'
                except:
                    traceback.print_exc()
                    return True, 4, ''

                return False, 0, remotefile
        else:
            r = requests.get(message.mentions[0].avatar_url, stream=True)
            if r.status_code == 200:
                with open(''.join(('tmp/', message.mentions[0].avatar_url.split('/')[-1].split('?')[0])), 'wb') as f:
                    for chunk in r:
                        f.write(chunk)

                filepath = ''.join(('tmp/', message.mentions[0].avatar_url.split('/')[-1].split('?')[0]))
                try:
                    picture = Image.open(filepath)
                except:
                    traceback.print_exc()
                    return True, 3, ''
                rand_discriminator = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(5))
                localfile = '/discordcdn/jpeg/' + message.channel.id + '/' + message.author.id + '/' + message.mentions[0].avatar_url.split('/')[-1].split('?')[0] + str(rand_discriminator) + '.jpg'
                if not os.path.exists('/discordcdn/jpeg/' + message.channel.id):
                    os.makedirs('/discordcdn/jpeg/' + message.channel.id)
                if not os.path.exists('/discordcdn/jpeg/' + message.channel.id + '/' + message.author.id):
                    os.makedirs('/discordcdn/jpeg/' + message.channel.id + '/' + message.author.id)
                try:
                    picture = picture.convert('RGB')
                    #picture = picture.filter(ImageFilter.UnsharpMask(80000,80000,0))
                    picture.save(localfile,"JPEG",optimize=False,quality=1)
                    remotefile = 'http://cdn.jplp.tk/jpeg/' + message.channel.id + '/' + message.author.id + '/' + message.mentions[0].avatar_url.split('/')[-1].split('?')[0] + str(rand_discriminator) + '.jpg'
                except:
                    traceback.print_exc()
                    return True, 4, ''

                return False, 0, remotefile
