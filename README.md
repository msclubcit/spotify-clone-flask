# Spotify Clone Application

## Requirements
* Programming language: `Python`
* Framework: `Flask`
* CSS Framework: `Bootstrap 5`
* SQL Database: `SQLite` for development

## How to build it - ToDo List

### Pages of Spotify music clone app

* **Static pages** - for user view
    * `home.html`
    * `about.html`
    * `contact.html`
    * `disclaimer.html`

* **Dynamic pages** - for users (using SQL)
    * `music-list.html`
    * `play-music.html`

* **Music Manager (Administrator)** - only for authenticated 
    * `admin/login.html`
    * `admin/register.html`
    * `admin/music/add.html`
    * `admin/music/list.html`
    * `admin/music/edit.html`
    * `admin/music/delete.html`
    * `admin/messages.html`

### Database Tables

* **Author**
    * `username` - TEXT | PK
    * `name` - TEXT 
    * `socialhandle` - TEXT (example: Instagram handle)
* **Album**
    * `slug` - TEXT | PK
    * `title` - TEXT
    * `author` - FK (Author | name)
* **Track**
    * `slug` - TEXT | PK
    * `title` - TEXT
    * `url` - TEXT
    * `album` - FK (Album | title)
    * `duration` - INTEGER (example: 1:00 -> 60 seconds)


### Mentor
* [Bharat Naik](https://github.com/bharatanaik)


### Contributors (MSCLUB Volunteers)
<!-- Task 1  -->
<!-- Each contributor must fork this repository and add his/her name into this readme file and should make a pull request -->
<!-- Example: [Timmy](https://github.com/timmyomahony) -->
* [Nikhil Kumar](https://github.com/Nikhil-Blllitz)
* [Rithvik K](https://github.com/Rithvikbng)
* [Dilip B](https://github.com/DILIP-SHEESH)
* [Harshitha M](https://github.com/Harshitham1204)
