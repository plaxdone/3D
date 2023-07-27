from PIL import Image

def fundo():
    im = Image.new(mode="RGB", size=(2950,2127), color = '#ffffff')
    img1 = Image.open('marcaNova.png')
    linha = coluna = alt = lar = 0
    while linha < 3:
        while coluna < 5:
            im.paste(img1, (lar,alt))
            coluna += 1
            lar += 590
        linha += 1
        lar = coluna = 0
        alt += 709



