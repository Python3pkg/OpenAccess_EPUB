"""contributor.py"""
from utils import getTagData, serializeText

class Contributor:
    """Represents a contributor to the article.
    In practical terms, this generally means either an Author,
    or an Editor when it comes to academic journalism.
    More may be added as necessary to this class.
    """
    def __init__(self, contribnode):
        self.surname = ''
        self.givenname = ''
        self.affiliation = []
        self.contact = []
        
        try:
            namenode = contribnode.getElementsByTagName('name')[0]
        except IndexError:
            pass
        else:
            self.surname = getTagData(namenode.getElementsByTagName('surname'))
            try:
                self.givenname = getTagData(namenode.getElementsByTagName('given-names'))
            except:
                pass
        
        try:
            collab_node = contribnode.getElementsByTagName('collab')[0]
        except IndexError:
            self.collab = None
        else:
            self.collab = 
        
        
        self.xrefs = contribnode.getElementsByTagName('xref')

        for ref in self.xrefs:
            reftype = ref.getAttribute('ref-type')
            if reftype == 'aff':
                self.affiliation.append(ref.getAttribute('rid'))
            elif reftype == 'corresp':
                self.contact.append(ref.getAttribute('rid'))

    def __str__(self):
        out = 'Surname: {0}, Given Name: {1}, AffiliationID: {2}, Contact: {3}'
        return out.format(self.surname, self.givenname,
                          self.affiliation, self.contact)

    def get_name(self):
        """Get the name. Formatted as: Carl Sagan"""
        if not self.collab:
            return(u'{0} {1}'.format(self.givenname, self.surname))
        else:
            return(serializeText(self.collab, stringlist = []))
    
    def get_fileas_name(self):
        '''Get the name. Formatted as: Sagan C'''
        names = self.givenname.split(' ')
        initials = ''
        for name in names:
            initials += name[0]
        return(u'{0}, {1}'.format(self.surname, initials))

class Author(Contributor):
    """Represents an author."""
    def __init__(self, contribnode):
        Contributor.__init__(self, contribnode)

class Editor(Contributor):
    """Represents an editor."""
    def __init__(self, contribnode):
        Contributor.__init__(self, contribnode)
