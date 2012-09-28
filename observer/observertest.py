from loan import loan
from newspaper import newspaper
from internet import internet
        
def main():
    l = loan()
    l.attach(newspaper())
    l.attach(internet())
    l.set_interest_rate(2.5)
    
if __name__ == "__main__":
    main()
