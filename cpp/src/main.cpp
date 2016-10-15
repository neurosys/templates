#include <iostream>

int main(int argc, char* argv[])
{
    std::cout << "Program = '" << argv[0] << "' argc = " << argc << std::endl;
    for (int i = 0; i < argc; i++)
    {
        std::cout << "argv[" << i << "] = '" << argv[i] << "'" << std::endl;
    }
    std::cout << "Hellow world" << std::endl;
    return 0;
}
