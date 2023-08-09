from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph

# Sample text containing references
# sample_text = [
#     "1.	B. Aboba, L. Blunk, J. Vollbrecht, J. Carlson, and H. Levkowetz, Extensible Authentication Protocol (EAP). Request for Comments: 3748, June 2004.",
#     "2.	Adi Shamir, Identity based cryptosystems and signatures, in Proceedings of Cryptology, Springer-Verlag, Berlin, 1984, pp. 47–53.BBBBB",
#     "3.	J.-L. Beuchat, E. Lpez-Trejo, L. Martnez-Ramos, S. Mitsunari, and F. Rodrguez-Henrquez, Multi-Core Implementation of the Tate Pairing Over Supersingular Elliptic Curves, Proceedings of the 8th International Conference in Cryptology and Network Security, 12– 14 December 2009.",
#     "4.	D. Boneh, and X. Boyen, Efficient selective-ID secure identity based encryption without random oracles, in Proc. of EUROCRYPT 04, LNCS, 3027, Springer Verlag, Interlaken, Switzerland, 2004, pp. 223–238.",
#     "5.	D. Boneh, and M. Franklin, Identity-based encryption from the weil pairing, in Proc. of CRYPTO 01, LNCS, 2139, Springer, Santa Barbara, CA, 2001, pp. 213–229.",
#     "6.	V. Cakulev, and I. Broustis, An EAP authentication method based on identity-based authenticated key exchange. draft-cakulev-emu-eap-ibake-03.txt, August 2012, work in progress 2012.",
#     "7.	V. Cakulev, G. Sundaram, and I. Broustis, IBAKE: identity-based authenticated key exchange, RFC 6539 2012. ISSN: 2070-1721.",
#     "8.	C. Ellison, and B. Schneier, Ten risks of PKI: what you’re not being told about public key infrastructure, Computer Security Journal 16(1) (2000), pp. 1–7.",
#     "10. V. Kolesnikov, and G.S. Sundaram, IBAKE: Identity-Based Authenticated Key Exchange Protocol, The International Association for Cryptologic Research (IACR), Cryptology ePrint Archive 2011.",
#     "11. Martijn Maas, Pairing-based cryptography. Master Thesis, Technische Universiteit Eindhoven 2004.",
#     "13. E. Rescorla, M. Ray, S. Dispensa, and N. Oskov, Transport Layer Security (TLS) Renegotiation Indication Extension, RFC 5746 2010.",
#     "14. M.F. Sadikin, and M. Kyas, RFID-Tate: Efficient Security and Privacy Protection for Active RFID Over IEEE 802.15.4. The 5th International Conference on Information, Intelligence, Systems and Applications, IISA 2014.",
#     "15. P. Szczechowiak, and M. Collier, Tinyibe: Identity-Based Encryption for Heterogeneous Sensor Networks, 5th International Conference on Intelligent Sensors, Sensor Networks, and Information Processing (ISSNIP), Melbourne, Australia, 2009, pp. 319–354.",
#     "16. Vladimir Kolesnikov, and Charles Rackoff, Key exchange using passwords and long keys, in Theory of Cryptography, TCC, volume 3876 of LNCS, Springer, Columbia University, New York, NY, USA, 2006, pp. 100–119.",
#     "17. Vladimir Kolesnikov, and Charles Rackoff, Password mistyping in two-factor- authenticated key exchange, in ICALP, Springer-Verlag, Reykjavik, Iceland, 2008, pp. 702–714.",
# ]
sample_text = [
    "D. Boneh, and X. Boyen, Efficient selective-ID secure identity based encryption without random oracles, in Proc. of EUROCRYPT 04, LNCS, 3027, Springer Verlag, Interlaken, Switzerland, 2004, pp. 223–238.~D. Boneh, and M. Franklin, Identity-based encryption from the weil pairing, in Proc. of CRYPTO 01, LNCS, 2139, Springer, Santa Barbara, CA, 2001, pp. 213–229. ~V. Cakulev, and I. Broustis, An EAP authentication method based on identity-based authenticated key exchange. draft-cakulev-emu-eap-ibake-03.txt, August 2012, work in progress 2012.~V. Cakulev, G. Sundaram, and I. Broustis, IBAKE: identity-based authenticated key exchange, RFC 6539 2012. ISSN: 2070-1721.~C. Ellison, and B. Schneier, Ten risks of PKI: what you’re not being told about public key infrastructure, Computer Security Journal 16(1) (2000), pp. 1–7.~V. Kolesnikov, and G.S. Sundaram, IBAKE: Identity-Based Authenticated Key Exchange Protocol, The International Association for Cryptologic Research (IACR), Cryptology ePrint Archive 2011.~Martijn Maas, Pairing-based cryptography. Master Thesis, Technische Universiteit Eindhoven 2004.~E. Rescorla, M. Ray, S. Dispensa, and N. Oskov, Transport Layer Security (TLS) Renegotiation Indication Extension, RFC 5746 2010.~M.F. Sadikin, and M. Kyas, RFID-Tate: Efficient Security and Privacy Protection for Active RFID Over IEEE 802.15.4. The 5th International Conference on Information, Intelligence, Systems and Applications, IISA 2014.~P. Szczechowiak, and M. Collier, Tinyibe: Identity-Based Encryption for Heterogeneous Sensor Networks, 5th International Conference on Intelligent Sensors, Sensor Networks, and Information Processing (ISSNIP), Melbourne, Australia, 2009, pp. 319–354.~Vladimir Kolesnikov, and Charles Rackoff, Key exchange using passwords and long keys, in Theory of Cryptography, TCC, volume 3876 of LNCS, Springer, Columbia University, New York, NY, USA, 2006, pp. 100–119.~Vladimir Kolesnikov, and Charles Rackoff, Password mistyping in two-factor- authenticated key exchange, in ICALP, Springer-Verlag, Reykjavik, Iceland, 2008, pp. 702–714."
]


def create_pdf(text, filename):
    # Create a new PDF document and add the text to it
    doc = SimpleDocTemplate(filename, pagesize=letter)
    styles = getSampleStyleSheet()
    story = [Paragraph(text, styles["Normal"])]
    doc.build(story)


# Generate separate PDF files for each entry in the sample_text list
for idx, text_entry in enumerate(sample_text, start=1):
    filename = f"{idx}.pdf"
    create_pdf(text_entry, filename)
    print(f"Document {idx} created as '{filename}'")
