Output minishell_demo.gif
Set FontSize 14
Set Width 1200
Set Height 800
Set Padding 20
Set Speed 1.0
    7
# 1. Entrar al contenedor
Type "42"
Enter
Sleep 3s  # Espera a que el contenedor cargue
   12
# 2. Ir a la carpeta del proyecto (ajusta la ruta si es necesario)
Type "cd path/to/Minishell"
Enter
Sleep 500ms
   17
# 3. Ejecutar los tests
Type "bash tester/run_tests.sh"
Enter
Sleep 1s
   22
# 4. Seleccionar opción 9 (Run All Mandatory)
Type "9"
Enter
   26
# Esperar a que terminen los tests (ajusta el tiempo)
Sleep 20s
   29
# 5. Salir del tester y del contenedor
Type "q"
Enter
Sleep 500ms
Type "exit"
Enter
