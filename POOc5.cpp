//Programa 5 del paradigama de objetos
#include<iostream>
using namespace std;

class libros
{
public:
    string titulo;
    string autor;
    int year;


    libros(string titulo, string autor, int year) : titulo(titulo), autor(autor), year(year){}
    void mostrar_inforamcion(); 
};



void libros::mostrar_inforamcion()
{
    cout << "Titulo de la obra: " << titulo <<std::endl;
    cout << "Autor de la obra: " << autor <<std::endl;
    cout << "Ano de publicacion de la obra: " << year <<std::endl;
}


int main()
{
    libros libro1("La fundacion", "Isaac Asimov", 1985);
    libros libro2("Cementerio de mascoras", "Sthephen King", 2000);
    libro1.mostrar_inforamcion();
    libro2.mostrar_inforamcion();
    system("Pause");
    return 0;
}
