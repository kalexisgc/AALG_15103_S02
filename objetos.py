"""
c#
class Perro{
    public string raza {get;set;}
    public string edad {get;set;}
    
    public Perro(){
        this.edad = 1;
    }
    public Perro(string raza){
        this.raza = raza;
        this.edad = 1;
    }
    public string ToString(){
        return $"{this.raza} de {this.edad} años"
    }
    public void Ladrar(){
        Console.WriteLine($"{this.raza} dice guau")
    }
}

Perro p = new Perro();
Perro q = new Perro("Chuguagua");
q.Ladrar()
"""
#python
class Perro:
    def __init__(self, raza = ""):
        self.raza = raza
        self.edad = 1
    def __str__(self):
        return f"{self.raza} de {self.edad} años"
    def ladrar(self):
        print(f"{self.raza} dice guau")

p = Perro()
print(p)
p.ladrar()

q = Perro("Chuguagua")
print(q)
q.ladrar()
