from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from random import randint

questions = {
	"IN WIE VIELEN LÄNDERN IST DAS KLEIDERGESCHÄFT TALLY WEIJL VERTRETEN?": "In 39 Ländern",
    "WO KANNST DU, UNTER ANDEREM, ENERGY AIR TICKETS GEWINNEN?": "Am Sender bei Radio Energy",
    "IN WELCHER LOCATION FINDET DAS ENERGY AIR 2021 UNTER FREIEM HIMMEL STATT?": "Stadion Wankdorf",
    "WIE HEISST DIE INITIATIVE FÜR MEHR RESPEKT IM INTERNET, WELCHE SWISSCOM MIT ENERGY LANCIERT HAT UND AM ENERGY AIR IHREN GROSSEN HÖHEPUNKT FEIERT?":"Mute the Hate",
    "WER WAR DER ALLERERSTE ACT IN DER GESCHICHTE DES ENERGY AIR?": "Bastian Baker",
    "WER WAR DER ÜBERRASCHUNGSACT AM ENERGY AIR 2018?": "Lo & Leduc",
    "IN WELCHEM SCHWEIZER KANTON ERÖFFNETE TALLY WEIJL 1987 DEN ERSTEN STORE?": "Basel",
    "MIT WELCHER ZUSATZOPTION HAST DU DIE MÖGLICHKEIT, DIREKT VOR DER BÜHNE ZU STEHEN?": "XTRA Circle",
    "WIE LANGE DAUERTE DAS ENERGY AIR 2019?": "6 Stunden",
    "MUSIKGRÖSSEN AUS WIE VIELEN LÄNDERN WAREN AM ENERGY AIR 2019 DABEI?": "Aus 7 Ländern",
    "WANN IST DIE TICKETVERLOSUNG FÜRS ENERGY AIR 2021 GESTARTET?": "Am 2. August 2021",
    "WELCHE ZWEI ENERGY KULTFIGUREN MISCHTEN DAS ENERGY AIR 2017 RICHTIG AUF?": "Tinu & Dänu",
    "WELCHE MUSIKERIN WURDE AM ENERGY AIR 2018 VON EINER 9-JÄHRIGE BESUCHERIN AUF DER BÜHNE GECOVERT?": "Namika",
    "NACH WELCHEM KRITERIUM WÄHLT DAS ENERGY TEAM DIE ACTS FÜR DAS ENERGY AIR AUS?": "Musiker*innen aus der aktuellen Energy Playlist",
    "WAS IST DAS PERFEKTE OPENAIR-OUTFIT?": 'Egal, hauptsache du kannst darin tanzen',
    "WAS FOLGT AM DIESJÄHRIGEN ENERGY AIR ALS KRÖNENDER ABSCHLUSS?": "Aftershowparty",
    "UNTER WELCHEM MOTTO FEIERN WIR AM 4. SEPTEMBER 2021 DAS ENERGY AIR?": "We are back.",
    "WAS PASSIERT, WENN ES AM ENERGY AIR REGNET?": "Der Event findet trotzdem statt",
    "VON WELCHER MARKE WAR DAS MOTORRAD, MIT DEM LOCO ESCRITO AM LETZTEN ENERGY AIR ÜBER DIE BÜHNE FUHR?": "Harley-Davidson",
    "MIT WELCHEM ESC-HIT ROCKTE LUCA HÄNNI AM LETZTEN ENERGY AIR DIE BÜHNE?": "She Got Me",
    "WIE HEISST DER OFFIZIELLE INSTAGRAM-ACCOUNT DES ENERGY AIR?": "@energyair_official",
    "IN WELCHEN FARBEN TRITT DAS ENERGY AIR LOGO JÄHRLICH FÜR DAS SOMMERFINALE AUF?": "Blau und Weiss",
    "WAS WAR DAS ERSTE, WAS KÜNSTLER KNACKEBOUL NACH SEINEM AUFTRITT 2014 BACKSTAGE GEMACHT HAT?": "Mit seinem Mami ein kühles Bier getrunken",
    "WELCHER KÜNSTLER MUSSTE AM LETZTEN ENERGY AIR BACKSTAGE EINEN PART AUS DEM DIALEKTRAPSONG VON SANDRO VORRAPPEN?": "Stress",
    "WELCHER ACT FEIERTE AM LETZTEN ENERGY AIR MIT EINEM NEUEN SONG EINE WELTPREMIERE?": "Aloe Blacc",
    "WIE KANNST DU DEINE GEWINNCHANCEN BEI TICKETVERLOSUNGEN FÜR ENERGY EVENTS VERDOPPELN?": "Mit einer Energy One Membership",
    "WIE ALT MUSS MAN SEIN, UM OHNE ERWACHSENE BEGLEITUNG AM ENERGY AIR TEILZUNEHMEN?": "14 Jahre",
    "WELCHE STADT GEHÖRT SEIT AUGUST AUCH ZUR ENERGY FAMILIE UND WIRD AM ENERGY AIR VERTRETEN SEIN?": "Luzern",
    "MIT WELCHEM AUFBLASBAREN TIER KONNTEN ZWEI AUSERWÄHLTE AM LETZTEN ENERGY AIR ÜBER DIE GANZE MEUTE CROWDSURFEN?": "Schwan",
    "WOMIT ERSCHIENEN DIE ENERGY MEIN MORGEN MODERATOREN MOSER UND SCHELKER AUF DER ENERGY AIR BÜHNE 2019?": "Mit Spielzeug-Pferden",
    "WELCHES SCHWEIZER DJ-DUO SORGTE AM ENERGY AIR 2019 ZU BEGINN FÜR REICHLICH STIMMUNG?": "Averdeck",
    "WIE HEISST DIE TRAM- UND BUSHALTESTELLE, WELCHE SICH DIREKT NEBEN DEM STADION WANKDORF BEFINDET?": "Wankdorf Center",
    "WELCHEN KLEIDUNGSSTIL VERFOLGT TALLY WEIJL GRUNDSÄTZLICH?": "Just in time (voll im Trend)",
    "WELCHER ACT WAR NOCH NIE AN EINEM ENERGY AIR DABEI?": "Cro",
    "WIE WIRD TALLY WEIJL AUSGESPROCHEN?": "Talli Weil",
    "IN WELCHER BELIEBTEN SERIE WAR TALLY WEIJL ZU SEHEN?": "Gossip Girl",
    "Du hast die erste Hürde geschafft.": "Jetzt Tickets für das Energy Air gewinnen!"
}


#init
with open("ini.txt") as f:
    path = f.readlines()
f.close()

options = webdriver.ChromeOptions()
options.add_argument(f"user-data-dir={path[0]}")
options.add_argument("--user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36")
driver = webdriver.Chrome(options=options)
driver.get("https://game.energy.ch/")
while True:
    try:
        while True:
            for i in range(10):
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/div/div/div/h3")))
                question = driver.find_element_by_xpath("//*[@id=\"app\"]/div/div[2]/div/div/div/div/h3").text
                answer = questions.get(question)
                answer_div = driver.find_element_by_xpath("//*[@id=\"answers\"]")
                answers = answer_div.find_elements_by_class_name("answer-wrapper")
                for i in answers:
                    solution = i.find_element_by_tag_name("input").get_attribute("id")
                    if solution == answer:
                        i.click()
                driver.find_element_by_xpath("//*[@id=\"next-question\"]").click()
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/div/div/div/div[2]/div[1]/div/div[1]/img")))
            driver.find_element_by_xpath("//*[@id=\"app\"]/div/div[2]/div/div/div/div/div[2]/div[1]/div/div[1]/img").click()
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"app\"]/div/div[2]/div/div/div[2]/div")))
            div_bubbles = driver.find_element_by_xpath("//*[@id=\"app\"]/div/div[2]/div/div/div[2]/div")
            bubbles = div_bubbles.find_elements_by_tag_name("img")
            zufall = randint(0, 11)
            bubbles[zufall].click()
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"lose\"]")))
            driver.find_element_by_xpath("//*[@id=\"lose\"]").click()
    except Exception:
        driver.find_element_by_xpath("//*[@id=\"app\"]/div/div[2]/div/div/button").click()
        print("Exception")
