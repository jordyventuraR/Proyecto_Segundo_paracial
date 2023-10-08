//Programa 6
#include<iostream>
using namespace std;
class Persona
{
public:
    string nombre;
    int edad;
    string clase;

    Persona(string nombre, int edad, string clase) : nombre(nombre), edad(edad), clase(clase) {}
    void datos();
};

void Persona::datos()
{
    cout << "Nombre: " << nombre <<std::endl;
    cout << "Edad: " << edad <<std::endl;
    cout << "clase: " << clase <<std::endl;
}


class Humano: public Persona
{
public:
    int energia;
    int fuerza;

    Humano(string nombre, int edad, int energia, int fuerza): Persona(nombre, edad, "Humano"), energia(energia), fuerza(fuerza){}
    void VerStats();
    void correr();
};

void Humano::VerStats(){
    Persona::datos();
    cout << "Energia: " << energia <<std::endl;
    cout << "Fuerza: " << fuerza <<std::endl;
}


void Humano::correr(){
    if (energia>=5)
    {
        energia -=5;
        cout << nombre << ": esta corriendo"<<std::endl;
    }else
    {
        cout << nombre << ": No puedo correr" <<std::endl;
    }
}

class Mago:  public Persona
{
public:
    int sabiduria;
    int mana;

    Mago(string nombre, int edad, int sabiduria, int mana): Persona(nombre, edad, "Mago"), sabiduria(sabiduria), mana(mana){}
    void verStats();
    void  Hechizo();
    void Descansar();
};


void Mago::verStats()
{
    Persona::datos();
    cout << "sabidura: " << sabiduria <<std::endl;
    cout << "mana: " << mana <<std::endl;
}

void Mago::Hechizo()
{
    mana-=5;
    std::cout << "El mado lanzo su hechizo" << std::endl;
}

void Mago::Descansar()
{
    mana+=5;
    std::cout << "El mago se esta recuperando"<< std::endl;
}


int main()
{
    Humano persona1("Pegre", 23, 60, 30);
    Mago brujo("Merlin", 45, 50, 10);
    int opcion;
    do
    {
        std::cout << "Seleccione una opcion: " << std::endl;
        std::cout << "1) Ver stats" << std::endl;
        std::cout << "2) Correr" << std::endl;
        std::cout << "3) Lanzar Hechizo" << std::endl;
        std::cout << "4) Descansar" << std::endl;
        std::cout << "5) Salir" << std::endl;
        cin>>opcion;
        switch (opcion)
        {
        case 1:
            std::cout << "Persona:" <<std::endl;
            persona1.VerStats();
            std::cout << "Mago:" << std::endl;
            brujo.verStats();
            break;
        
        case 2:
            persona1.correr();
            break;

        case 3:
            brujo.Hechizo();
            break;

        case 4:
            brujo.Descansar();
            break;

        case 5:
            std::cout << "Gracias por usar el programa" << std::endl;
            break;
        
        default:
            std::cout << "Opcion errorenea" << std::endl;
            break;
        }

    } while (opcion!=5);
    system("Pause");
    return 0;
}

