Kurmanız gerekenler
- Python. (Selenium'u python ile kullanıldı.)
- Selenium. (burada 4.19.0 kullanıldı.)
- pip install selenium (Last kurar daha öncesinde https://www.selenium.dev/downloads/ sitesine gidip en son kararlı sürüm hangisi ise onu kurmanızı öneriyorum ben kendim kurduğum vakitte 4.19.0'dı. Eğer son sürüm kararlı değilse şu şekilde kurulum yapabilirsiniz. "pip install selenium==x.x.x)


 
- Web driver. (Selenium web driver kullandığından kaynaklı. Ben burada chrome driver kullandım çünkü artık bu bir klasik olmuş durumda. https://chromedriver.chromium.org/downloads buraya gidip kendi kullandığınız chrome versiyonuna göre indirime işlemini yapabilirsiniz. Chrome ayarlar->chrome hakkında kısmından hangi versiyonu kullandığınızıda kolayca öğrenebilirsiniz.)

Yada benim projede kullandığım gibi otomatik kullanabilirsiniz (Kullanımını projede görebilirsiniz) :
- pip install chromedriver-autoinstaller (sizin yerinize şuan sizde kurulu olan chrome sürümü ile uyumlu driver'ı kuracaktır. import ederek kullanıyoruz <3)