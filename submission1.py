from gtts import gTTS
from playsound import playsound
import sys


def speak(filename, text):
    tts = gTTS(text, lang='en')
    tts.save(filename + '.mp3')
    playsound(filename + '.mp3')


speak('Hello! Welcome to this biotech app!', '111')

speak("Please enter 1 if you want to find genes in a dna sequence. Enter 2 to find air quality health index", '114')

command1 = input("Please enter 1 if you want to find first gene in a dna sequence. Enter 2 to find air quality health index")


def find_gene(filename):
    with open(filename + '.txt', 'r') as file1:
        dna = file1.read()
        if 'ATG' not in dna:
            print('No gene found. System exiting....')
            print("Press any key to exit....")
            input()
            sys.exit()
        else:
            codon_start = dna.index('ATG')

        if 'TAA' in dna:
            if 'TAG' in dna and dna.index('TAG', codon_start + 3) < dna.index('TAA', codon_start + 3):
                if 'TGA' in dna and dna.index('TGA', codon_start + 3) < dna.index('TAG', codon_start + 3):
                    stop_codon = dna.index('TGA')
                else:
                    stop_codon = dna.index('TAG')
            elif 'TGA' in dna and dna.index('TGA', codon_start + 3) < dna.index('TAA', codon_start + 3):
                if 'TAG' in dna and dna.index('TAG', codon_start + 3) < dna.index('TGA', codon_start + 3):
                    stop_codon = dna.index('TAG')
                else:
                    stop_codon = dna.index('TGA')
            else:
                stop_codon = dna.index('TAA')
        elif 'TGA' in dna:
            if 'TAG' in dna and dna.index('TAG') < dna.index('TGA'):
                stop_codon = dna.index('TAG')
            else:
                stop_codon = dna.index('TGA')
        elif 'TAG' in dna:
            if 'TGA' in dna and dna.index('TGA') < dna.index('TAG'):
                stop_codon = dna.index('TGA')
            else:
                stop_codon = dna.index('TAG')
        else:
            print('No gene found. System exiting....')
            print('Enter any key to exit....')
            input()
            sys.exit()

        gene = dna[start_codon:stop_codon]

        print('The following is the first gene found: ', '\n', gene)

def airqualityindex(o3, no2, pm):
    import requests

    url = "https://carbonfootprint1.p.rapidapi.com/AirQualityHealthIndex"

    querystring = {"O3": o3, "NO2": no2, "PM": pm}

    headers = {
        'x-rapidapi-key': "c9a50d71bbmsh986ce6928856767p1381e8jsn95185302faab",
        'x-rapidapi-host': "carbonfootprint1.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)

if command1 == '1':
    speak('Please enter the .txt filename containing the dna sequence only', '112')
    dna_file = input("Please enter the .txt filename containing the dna sequence only: ")
    find_gene(dna_file)

if command1 == '2':
    o3 = int(input("Enter the ppm quantity of o3: "))
    no2 = int(input("Enter the ppm quantity of no2: "))
    pm = int(input("Enter the ppm quantity of pm: "))
    print('Air Quality Health Index:-')
    airqualityindex(o3, no2, pm)
