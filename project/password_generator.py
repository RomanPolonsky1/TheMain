import random
import uuid
import hashlib
general_text = """
Global citizenship education[edit]
Main article: Global citizenship education
Within the educational system, the concept of global citizenship education (GCED) is beginning to supersede or overarch movements such as multicultural education, peace education, human rights education, Education for Sustainable Development, and international education.[5] Additionally, GCED rapidly incorporates references to the aforementioned movements. The concept of global citizenship has been linked with awards offered for helping humanity.[6] Teachers are being given the responsibility of being social change agents.[7] Audrey Osler, director of the Centre for Citizenship and Human Rights Education, the University of Leeds, affirms that "Education for living together in an interdependent world is not an optional extra, but an essential foundation".[8]

With GCED gaining attention, scholars are investigating the field and developing perspectives. The following are a few of the more common perspectives:

Critical and transformative perspective. Citizenship is defined by being a member with rights and responsibilities. Therefore, GCED must encourage active involvement. GCED can be taught from a critical and transformative perspective, whereby students are thinking, feeling, and doing. In this approach, GCED requires students to be politically critical and personally transformative. Teachers provide social issues in a neutral and grade-appropriate way for students to understand, grapple with, and do something about.[9]
Worldmindedness. Graham Pike and David Selby view GCED as having two strands. Worldmindedness, the first strand, refers to understanding the world as one unified system and a responsibility to view the interests of individual nations with the overall needs of the planet in mind. The second strand, Child-centeredness, is a pedagogical approach that encourages students to explore and discover on their own and addresses each learner as an individual with inimitable beliefs, experiences, and talents.[10]
Holistic Understanding. The Holistic Understanding perspective was founded by Merry Merryfield, focusing on understanding the self in relation to a global community. This perspective follows a curriculum that attends to human values and beliefs, global systems, issues, history, cross-cultural understandings, and the development of analytical and evaluative skills.[7]
Philosophy[edit]
Global citizenship, in some contexts, may refer to a brand of ethics or political philosophy in which it is proposed that the core social, political, economic, and environmental realities of the world today should be addressed at all levels—by individuals, civil society organizations, communities, and nation states—through a global lens. It refers to a broad, culturally and environmentally inclusive worldview that accepts the fundamental interconnectedness of all things. Political, geographic borders become irrelevant and solutions to today's challenges are seen to be beyond the narrow vision of national interests. Proponents of this philosophy often point to Diogenes of Sinope (c. 412 B.C.) as an example, given his reported declaration that "I am a citizen of the world (κοσμοπολίτης, cosmopolites)" in response to a question about his place of origin.[11] A Tamil term, Yadhum oore yaavarum kelir, has the meaning of "the world is one family". The statement is not just about peace and harmony among the societies in the world, but also about a truth that somehow the whole world has to live together like a family.[12]
"""

tokenize_text = general_text.split()

def password_from_X_words(number_of_words=3):
    chosen = str(random.choice(tokenize_text))
    for i in range(number_of_words-1):
        chosen += str("-")+str(random.choice(tokenize_text))
    return chosen


chosen_x_words = password_from_X_words()
print(chosen_x_words)


def password_as_uuid():
    return uuid.uuid4()

uuidpass = password_as_uuid()
print(uuidpass)

