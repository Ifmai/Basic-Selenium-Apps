### Selenium Nedir?

Selenium, web tabanlı uygulamaların otomatik test edilmesi için kullanılan bir araçtır. Genellikle web tarayıcıları üzerinde test senaryolarını otomatik olarak çalıştırmak için kullanılır. Selenium, web tarayıcıları ile etkileşim kurabilen bir test otomasyon aracıdır ve çeşitli programlama dilleriyle (Python, Java, C#, vb.) kullanılabilir.

Selenium, temel olarak şu üç ana bileşeni içerir:

1. Selenium WebDriver: Gerçek tarayıcıları kontrol ederek test senaryolarını çalıştırmak için kullanılan bir API'dir. Farklı tarayıcılar için farklı WebDriver'lar bulunur (ChromeDriver, GeckoDriver, EdgeDriver, vb.).

2. Selenium IDE (Integrated Development Environment): Bu bir tarayıcı eklentisidir ve kullanıcıların test senaryolarını kaydetmelerine, düzenlemelerine ve oynamalarına olanak tanır. Selenium IDE, sık kullanılan web tarayıcılarında (örneğin, Chrome ve Firefox) kullanılabilir.

3. Selenium Grid: Bu, test senaryolarının paralel olarak farklı tarayıcılarda veya farklı platformlarda (işletim sistemleri ve tarayıcılar) çalıştırılmasını sağlayan bir bileşendir. Bu, test sürelerini azaltmaya ve test kapsamını artırmaya yardımcı olur.

Selenium, web uygulamalarının farklı bileşenlerini (örneğin, butonlar, metin kutuları, linkler) tanıyabilir, bu bileşenler üzerinde etkileşimler yapabilir (tıklama, metin girişi, sayfa gezinme), form doldurabilir ve sayfa özelliklerini (örneğin, başlık, URL) kontrol edebilir. Bu özellikleri sayesinde Selenium, web uygulamalarının doğruluğunu, performansını ve kullanılabilirliğini test etmek için geniş bir kullanım alanına sahiptir.

### Bu projede neler görüceksiniz?

Selenium da basit 17 adet küçük uygulama görüceksiniz. Bu uygulamaların amacı size selenium da önemli olan şeyleri nasıl yapıcağınızı göstermek amacıyla yazılmış örnekler görüceksiniz.

### Kullanımın için zorunluluklar;
- Python. (Selenium'u python ile kullanıldı.)
- Selenium. (burada 4.19.0 kullanıldı.)
- pip install selenium (Last kurar daha öncesinde https://www.selenium.dev/downloads/ sitesine gidip en son kararlı sürüm hangisi ise onu kurmanızı öneriyorum ben kendim kurduğum vakitte 4.19.0'dı. Eğer son sürüm kararlı değilse şu şekilde kurulum yapabilirsiniz. "pip install selenium==x.x.x)


- Web driver. (Selenium web driver kullandığından kaynaklı. Ben burada chrome driver kullandım çünkü artık bu bir klasik olmuş durumda. https://chromedriver.chromium.org/downloads buraya gidip kendi kullandığınız chrome versiyonuna göre indirime işlemini yapabilirsiniz. Chrome ayarlar->chrome hakkında kısmından hangi versiyonu kullandığınızıda kolayca öğrenebilirsiniz.)

Yada benim projede kullandığım gibi otomatik kullanabilirsiniz (Kullanımını projede veya aşağıdaki linkten görebilirsiniz.) :
- pip install webdriver-manager (sizin yerinize şuan sizde kurulu olan chrome sürümü ile uyumlu driver'ı kuracaktır. import ederek kullanıyoruz <3)
https://pypi.org/project/webdriver-manager/