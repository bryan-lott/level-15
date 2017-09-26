# level-15
Digital representation of 3x5" notecards with dual-pane modal editing and searching.

## Project Status
* Incomplete
* On-hold for the time being while I evaluate a commercial product ([Workflowy](https://workflowy.com)) that may give me what I was looking for from this project.

### Visual depiction:
* Split screen.  
* Right hand side is a text editor similar to ipython with "cards".  Used for stream-of-consciousness writing.
* Left hand side is a multi-document viewer.  Automatically surfaces documents as it finds connections to the writing on the right hand side.

### Ideas
* Can be entirely keyboard or mouse driven.
* Cards on the right hand side represent nodes in the graph
* Cards are separated by (either) `-----------` or > 1 carriage return
* Left hand side documents can be edited on the right hand side by selecting them (clicking or selecting via keyboard)
* <esc> switches between right and left panes(?)
* Vim keybindings?

### Initial Tech Decisions
* neo4j graph database
* python 3.6

### MVP
* create a node w/ an id and textual data
* associate a node with other nodes manually
* edit associations on an existing node
  
 
## Development

### Virtualenv

```bash
virtualenv -p /usr/local/bin/python3 .
source bin/activate.fish
pip3 install -r requirements.txt
```

### Docker

```bash
docker-compose build
docker-compose up
```
