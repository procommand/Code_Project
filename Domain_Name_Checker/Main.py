#pip3 install python-whois
#python3 -m pip install whois
#pip3  install whois
import whois

words = ["cabriolet","carriage","charabanc","chariot","coupé","Dormobile", "kibitka", "komatik","landaulet", "motorcar","tourer", "trolley", "Mawshein", "mashina", 
"Mashin", "machine"]

for word in words:
    
    print("New word ******************\n")
    new_word = ""
    for count in range(len(word)):
        new_word = (word[:count]+word[count+1:]+word[count])
        try:
            new_word_registered= (whois.whois(new_word+".com"))
        except whois.parser.PywhoisError:
            print("Domain name not registed: "+new_word+".com") #Domain not registered
        else:
            print("Registered: ",new_word_registered["domain_name"]) #Domain name registered
        
