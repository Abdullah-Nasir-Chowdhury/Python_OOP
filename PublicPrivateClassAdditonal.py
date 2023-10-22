import PublicPrivateClasses
from PublicPrivateClasses import NotPrivate

test = NotPrivate('tim')
"""since theres an underscore before the name of the method it's private
but it's still accessible. so you'd better not mess with it."""
test._display()
test.display()