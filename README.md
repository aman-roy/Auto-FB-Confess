# Auto FB Confess

A simple flask based app which helps in posting to FB pages automatically. It can be used to post directly to FB pages without any use of middle man.
<hr>

### Previous default approach for FB confession page
1. Create a FB confession page.
2. Create a google forms too.
3. Share the link of google form where people will confess.
4. Now admin will copy and paste the messages from google forms too facebook pages.
> This is very wrong approach. For this, admin has to do work. Interference is there. We need a approach which is fully secure and doesn't require any manual effort.

### My approach
1. Create a FB confession page.
2. Using FB SDK API, connect it to this single paged flask web app and share this link to everyone.
3. Now everything will be automated. As soon as someone write something on this webapp, it will be directly posted to the FB confession page.

### Try this yourself!

Use this link to post anonymously : - http://autofbconfess.amanroy.me
Use this link to see your posts : - https://www.facebook.com/Auto-FB-Confess-1029647553839937/

### Deployment
> For deploying locally - [See this](#)

> For deploying on Heroku - [See this](#)

### Contributing

All contributions and suggestions are welcome!

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request