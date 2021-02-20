# level-15

[idea] Digital representation of 3x5" notecards with modal editing and searching

- [ ] Basic functionality
  - [ ] Write in a small card (tweet or 3x5" notecard size)
  - [ ] Save cards
  - [ ] Link cards to one another explicitly
- [ ] Markdown
- [ ] Search as you write
- [ ] Automated backlinks
- [ ] Save as you write
- [ ] Versioning of saves
- [ ] Fuzzy search
- [ ] Modal editing (vim style)

## Project Status

- Just getting off the ground?

## Visual depiction

- Split screen.  
- Right hand side is a text editor similar to ipython with "cards".  Used for stream-of-consciousness writing.
- Left hand side is a multi-document viewer.  Automatically surfaces documents as it finds connections to the writing on the right hand side.

## Ideas

- Can be entirely keyboard or mouse driven.
- Cards on the right hand side represent nodes in the graph
- Cards are separated by (either) `-----------` or > 1 carriage return
- Left hand side documents can be edited on the right hand side by selecting them (clicking or selecting via keyboard)
- esc switches between right and left panes(?)
- Vim keybindings?

## Dependencies

- DearPyGUI
  - Python GUI that doesn't seem to suck
  - [documentation](https://github.com/hoffstadt/DearPyGui/wiki)
  - [blog post/tutorial](https://medium.com/datadriveninvestor/create-quick-and-powerful-guis-using-dear-pygui-in-python-713cc138bf5a)

![requirements.txt](./requirements.txt)
