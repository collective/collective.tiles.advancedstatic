from zope.schema.interfaces import IVocabularyFactory
from zope.component import getUtility
from plone.registry.interfaces import IRegistry
from zope.schema.vocabulary import SimpleTerm, SimpleVocabulary
from zope.interface import implementer


@implementer(IVocabularyFactory)
class CSSVocabulary(object):
    def keyfunction(self, item):
        """Key for comparison by last name"""
        return item.title

    def __call__(self, context):
        items = []
        registry = getUtility(IRegistry)
        styles = registry['collective.tiles.advancedstatic.css_styles']
        for style in styles:
            term = style.split('|')  # get value and title
            items.append(SimpleTerm(term[0], term[0], term[1]))
        items.sort(key=self.keyfunction)
        return SimpleVocabulary(items)


CSSVocabulary = CSSVocabulary()
