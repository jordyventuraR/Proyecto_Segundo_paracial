//Clase 4 del paradigma de objetos
#include<iostream>
using namespace std;
//Clase
class Cuenta_bancaria
{
public:
    //Atributos
    string titular;
    double saldo;

    Cuenta_bancaria(string titular, double saldo) : titular(titular), saldo(saldo){}
    //Metodos
    double depositar(double cantidad);
    double retirar(double cantidad);
};

//Metodo de depositar
double Cuenta_bancaria::depositar(double cantidad)
{
    saldo += cantidad;
    return saldo;
}

//Metodo de retirar
double Cuenta_bancaria::retirar(double cantidad)
{
    if (saldo<cantidad)
    {
        cout << "No tiene el saldo suficiente" <<endl;
        return saldo;
    
    }else{
        saldo -= cantidad;
        return saldo;
    }
}



int main()
{
    //Objeto
    Cuenta_bancaria Persona1("Juan", 300);
    cout << "Su saldo es: " << Persona1.depositar(200.0) <<std::endl;
    cout << "Su saldo es: " << Persona1.retirar(300.0)<<std::endl;
    cout << "Su saldo es: "<< Persona1.retirar(300.0) <<std::endl;

    system("Pause");
    return 0;
}
