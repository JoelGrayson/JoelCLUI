### Demo
```python
import joelclui as jclui

jclui.print('2+2=[green]4[/] and 3+3=[bg red]6[/]')
jclui.print('[yellow]Warning. [red][underline]Error[/] [green]Success[/]')
jclui.print('[bg blue][yellow]Colorful[/] Back to normal')

jclui.print('Status: TBD')
jclui.move_up()
jclui.print('[bold]Status: [green]Complete[/]')
```
Output:
![Terminal output image](https://w.joelgrayson.com/image/joelclui%20demo.jpg)
### Colors
Wrap on of the modifiers below in square brackets [] to change the printed text's style.
* Colors
    * `bold`
    * `green`
    * `yellow`
    * `red`
    * `blue`
    * `black`
    * `orange`
    * `purple`
    * `cyan`
    * `lightgray`
    * `darkgray`
    * `pink`
    * `lightred`
    * `lightgreen`
    * `lightblue`
    * `lightcyan`
    * `success`
    * `warn`
    * `danger`
* Backgrounds
    * `bg black`
    * `bg red`
    * `bg green`
    * `bg orange`
    * `bg blue`
    * `bg purple`
    * `bg cyan`
    * `bg lightgray`
* Styles
    * `[/]` clears the console
    * `bold`
    * `underline`

### Arrow navigation methods:
Optional parameter of how many times to move.
```python
jclui.move_up() #moves cursor up one line
jclui.move_right()
jclui.move_down()
jclui.move_left()

jclui.move_up(5) #Up 5 lines
```