testfields = {
    "principal_name": "Jasper Floppydog",
    "agent_list": "Emma Dog, Charlie Dog, and Ginger Dog",
    "empty_line": ("_" * 100),
    "joint_powers": "SEPARATELY",
    "signature_line": ("_" * 30),
    "day_num": "30th",
    "month": "February",
    "year": "2020",
    "notarization_state": "CA",
    "notarization_county": "Butte",
    "empty_field": ("_" * 20),
}

preamble = """NOTICE: THE POWERS GRANTED BY THIS DOCUMENT ARE BROAD AND SWEEPING. THEY ARE EXPLAINED IN THE UNIFORM STATUTORY FORM POWER OF ATTORNEY ACT (CALIFORNIA PROBATE CODE SECTIONS 4400-4465). THE POWERS LISTED IN THIS DOCUMENT DO NOT INCLUDE ALL POWERS THAT ARE AVAILABLE UNDER THE PROBATE CODE. ADDITIONAL POWERS AVAILABLE UNDER THE PROBATE CODE MAY BE ADDED BY SPECIFICALLY LISTING THEM UNDER THE SPECIAL INSTRUCTIONS SECTION OF THIS DOCUMENT. IF YOU HAVE ANY QUESTIONS ABOUT THESE POWERS, OBTAIN COMPETENT LEGAL ADVICE. THIS DOCUMENT DOES NOT AUTHORIZE ANYONE TO MAKE MEDICAL AND OTHER HEALTH-CARE DECISIONS FOR YOU. YOU MAY REVOKE THIS POWER OF ATTORNEY IF YOU LATER WISH TO DO SO.
"""
appointment = """I, [principal_name], appoint [agent_list] as my agent (attorney-in-fact) to act for me in any lawful way with respect to the following initialed subjects:
"""

preamble2 = """TO GRANT ALL OF THE FOLLOWING POWERS, INITIAL THE LINE IN FRONT OF (N) AND IGNORE THE LINES IN FRONT OF THE OTHER POWERS. TO GRANT ONE OR MORE, BUT FEWER THAN ALL, OF THE FOLLOWING POWERS, INITIAL THE LINE IN FRONT OF EACH POWER YOU ARE GRANTING. TO WITHHOLD A POWER, DO NOT INITIAL THE LINE IN FRONT OF IT. YOU MAY, BUT NEED NOT, CROSS OUT EACH POWER WITHHELD."""

form = """INITIAL
___ (A) Real property transactions.
___ (B) Tangible personal property transactions.
___ (C) Stock and bond transactions.
___ (D) Commodity and option transactions.
___ (E) Banking and other financial institution transactions.
___ (F) Business operating transactions.
___ (G) Insurance and annuity transactions.
___ (H) Estate, trust, and other beneficiary transactions.
___ (I) Claims and litigation.
___ (J) Personal and family maintenance.
___ (K) Benefits from social security, Medicare, Medicaid, or other governmental programs, or civil or military service.
___ (L) Retirement plan transactions.
___ (M) Tax matters.
___ (N) ALL OF THE POWERS LISTED ABOVE.
"""

supplement = """YOU NEED NOT INITIAL ANY OTHER LINES IF YOU INITIAL LINE (N).

SPECIAL INSTRUCTIONS:
ON THE FOLLOWING LINES YOU MAY GIVE SPECIAL INSTRUCTIONS LIMITING OR EXTENDING THE POWERS GRANTED TO YOUR AGENT.

[empty_line]

[empty_line]

UNLESS YOU DIRECT OTHERWISE ABOVE, THIS POWER OF ATTORNEY IS EFFECTIVE IMMEDIATELY AND WILL CONTINUE UNTIL IT IS REVOKED.
"""

incapacity = """This power of attorney will continue to be effective even though I become incapacitated.

"""

durable_strike = """STRIKE THE PRECEDING SENTENCE IF YOU DO NOT WANT THIS POWER OF ATTORNEY TO CONTINUE IF YOU BECOME INCAPACITATED.  """
multiple_agent = """EXERCISE OF POWER OF ATTORNEY WHERE MORE THAN ONE AGENT DESIGNATED
If I have designated more than one agent, the agents are to act [joint_powers].
"""


signature_block = """I agree that any third party who receives a copy of this document may act under it. A third party may seek identification. Revocation of the power of attorney is not effective as to a third party until the third party has actual knowledge of the revocation. I agree to indemnify the third party for any claims that arise against the third party because of reliance on this power of attorney.

Signed this [day_num] day of [month], [year].


[signature_line]
[principal_name]
State of [notarization_state], County of [notarization_county] 

BY ACCEPTING OR ACTING UNDER THE APPOINTMENT, THE AGENT ASSUMES THE FIDUCIARY AND OTHER LEGAL RESPONSIBILITIES OF AN AGENT.

"""

notary_box = """CERTIFICATE OF ACKNOWLEDGMENT OF NOTARY PUBLIC
A notary public or other officer completing this certificate verifies only the identity of the individual who signed the document to which this certificate is attached, and not the truthfulness, accuracy, or validity of that document.
"""

notary_ack = """State of California
County of [notarization_county]

On [empty_field] before me, [empty_field][empty_field], personally appeared [principal_name], who proved to me on the basis of satisfactory evidence to be the person(s) whose name(s) is/are subscribed to the within instrument and acknowledged to me that he/she/they executed the same in his/her/their authorized capacity(ies), and that by his/her/their signature(s) on the instrument the person(s), or the entity upon behalf of which the person(s) acted, executed the instrument.

I certify under PENALTY OF PERJURY under the laws of the State of California that the foregoing paragraph is true and correct.

WITNESS my hand and official seal:





[signature_line]
Notary Public
"""
