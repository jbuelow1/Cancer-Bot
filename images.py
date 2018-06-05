import requests
import ast
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
                    return True, 3, ''
                localfile = '/discordcdn/' + message.channel.id + '/' + message.author.id + '/' + url['filename'] + '.jpg'
                try:
                    picture = picture.convert('RGB')
                    picture = picture.filter(ImageFilter.UnsharpMask(80000,80000,0))
                    picture.save(localfile,"JPEG",optimize=False,quality=1)
                    remotefile = 'http://cdn.jplp.tk/' + message.channel.id + '/' + message.author.id + '/' + url['filename'] + '.jpg'
                except:
                    return True, 4, ''

                return False, 0, remotefile
            else:
                return True, 2, ''
        else:
            return True, 1, ''
    else:
        return True, 1, ''

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
                    return True, 3, ''
                localfile = '/discordcdn/' + message.channel.id + '/' + message.author.id + '/' + url['filename'] + '.jpg'
                try:
                    picture = picture.convert('RGB')
                    #picture = picture.filter(ImageFilter.UnsharpMask(80000,80000,0))
                    picture.save(localfile,"JPEG",optimize=False,quality=1)
                    remotefile = 'http://cdn.jplp.tk/' + message.channel.id + '/' + message.author.id + '/' + url['filename'] + '.jpg'
                except:
                    return True, 4, ''

                return False, 0, remotefile
            else:
                return True, 2, ''
        else:
            return True, 1, ''
    else:
        return True, 1, ''
