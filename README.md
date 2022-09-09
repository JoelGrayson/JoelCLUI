# Joel Command Line User Interface (JoelClui)
A command line user interface tool.


### Demo
```python
import joelclui as j

j.print('2+2=[green]4[/] and 3+3=[bg red]6[/]')
j.print('[yellow]Warning. [red][underline]Error[/] [green]Success[/]')
j.print('[bg blue][yellow]Colorful[/] Back to normal')

j.print('Status: TBD')
j.move_up()
j.print('[bold]Status: [green]Complete[/]')

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
j.move_up() #moves cursor up one line
j.move_right()
j.move_down()
j.move_left()

j.move_up(5) #Up 5 lines
```