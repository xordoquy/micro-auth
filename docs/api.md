# User API

## User list

Input message:

    user.list()

Output message:

    [{
        'username': '<username1>'
    }, {
        'username': '<username2>'
    }]


## User details

Input message:

    user.details("<username>")

&lt;username&gt; may contain wildcard that will be interpreted as search
parameters.

Output message:

    [{
        'username': '<username>',
        'firstname': '<firstname>',
        'lastname': '<lastname>',
        'email': '<email>'
    }]

Note that depending on the search criteria, you may have several users
representation as dictionnaries.


## User creation

Input message:

    user.new("{
        'username': '<username>',
        'firstname': '<firstname>',
        'lastname': '<lastname>',
        'email': '<email>'
    }")

Output message:

    [{
        'username': '<username>',
        'firstname': '<firstname>',
        'lastname': '<lastname>',
        'email': '<email>'
    }]


## User modification

Input message:

    user.update("<username>", "{
        'username': '<username>',
        'firstname': '<firstname>',
        'lastname': '<lastname>',
        'email': '<email>'
    }")

Output message:

    [{
        'username': '<username>',
        'firstname': '<firstname>',
        'lastname': '<lastname>',
        'email': '<email>'
    }]


## User deletion

Input message:

    user.delete()

Output message:

    ''
