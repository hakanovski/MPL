**ONTOLOGY.md

Magus Lineage → MPL Standard Library Mapping (v1.0)**

This document defines how the 225 historical magus lineages, as listed in MANIFESTO.md, are translated into MPL’s computational architecture.
Each lineage contributes to the design of:
	•	Standard Library modules
	•	Domain primitives
	•	Semantic patterns
	•	Ritual constructs (Invoke → Bind → Shape → Release)

The ontology forms the symbolic backbone of the Magick Programming Language.

⸻

1. Ontology Structure

For each cultural lineage, this ontology defines:
	1.	Primary Focus
	2.	Mapped stdlib modules
	3.	Canonical primitives introduced
	4.	Symbolic influence on syntax

All modules follow the canonical structure:

stdlib/<namespace>/<module>.ms

Primitives follow:

namespace.operation()


⸻

2. Cultural Lineages → stdlib Mapping

⸻

A) The Hermetic Core → std/hermetic/

Primary Focus:
Sigils, planetary hours, ceremonial evocation, alchemy, Enochian calls.

Modules:
	•	hermetic/seal.ms
	•	hermetic/enochian.ms
	•	hermetic/goetia.ms
	•	hermetic/alchemy.ms

Primitives:
	•	seal(...)
	•	sigil.draw()
	•	angelic.call()
	•	planetary.hour()
	•	triangle.art()

⸻

B) Slavic / Russian Psychic Tradition → std/psychic/

Primary Focus:
Telepathy, bio-field projection, remote influence.

Modules:
	•	psychic/remote_influence.ms
	•	psychic/psi_field.ms

Primitives:
	•	psi.emit()
	•	mind.channel()
	•	biofield.push()

⸻

C) Turkic / Anatolian / Central Asian Shamanism → std/shamanic/

Primary Focus:
Ancestor-channeling, nature-binding, dream-paths.

Modules:
	•	shamanic/ancestor.ms
	•	shamanic/nature_spirit.ms
	•	shamanic/dreampath.ms

Primitives:
	•	ancestor.call()
	•	wind.invoke()
	•	dream.enter()

⸻

D) Ancient Egyptian Necromantic Tradition → std/heka/

Primary Focus:
Death rites, mummification fields, heka formula structures.

Modules:
	•	heka/preservation.ms
	•	heka/funeral_rites.ms

Primitives:
	•	ka.bind()
	•	heka.formula()
	•	mummy.field()

⸻

E) Kabbalistic / Jewish Mysticism → std/kabbalah/

Primary Focus:
Gematria logic, divine names, textual metaphysics.

Modules:
	•	kabbalah/gematria.ms
	•	kabbalah/names.ms

Primitives:
	•	name.permute()
	•	golem.construct()
	•	sefirot.map()

⸻

F) Arab / Islamic Occult Science → std/djinn/

Primary Focus:
Talismanic diagrams, djinn-binding protocols, abjad numerology.

Modules:
	•	djinn/talisman.ms
	•	djinn/binding.ms
	•	djinn/abjad.ms

Primitives:
	•	talisman.draw()
	•	djinn.bind()
	•	abjad.compute()

⸻

G) Vedic / Himalayan Tradition → std/mantra/

Primary Focus:
Mantras, yantras, prana routing, siddhi operations.

Modules:
	•	mantra/chant.ms
	•	mantra/yantra.ms
	•	mantra/prana.ms

Primitives:
	•	chant("OM")
	•	prana.route()
	•	yantra.draw()

⸻

H) East Asian Sorcery (Japan/China/Korea) → std/onmyoji/

Primary Focus:
Shikigami, fu talismans, elemental routing.

Modules:
	•	onmyoji/shikigami.ms
	•	onmyoji/fu.ms
	•	onmyoji/elements.ms

Primitives:
	•	fu.draw()
	•	shikigami.call()
	•	element.route()

⸻

I) African Vodun, Fetish, Ancestor Rituals → std/vodun/

Primary Focus:
Spirit mounting, possession, inkisi engineering.

Modules:
	•	vodun/loa.ms
	•	vodun/possession.ms
	•	vodun/inkisi.ms

Primitives:
	•	loa.mount()
	•	ashe.flow()
	•	fetish.build()

⸻

J) Nordic / Scandinavian Runic Tradition → std/runes/

Primary Focus:
Rune carving, galdr chants, fate-warping.

Modules:
	•	runes/elder_futhark.ms
	•	runes/galdr.ms

Primitives:
	•	rune.carve()
	•	galdr.sing()
	•	fate.twist()

⸻

K) Native American / Polynesian Dream & Weather Lore → std/dreamwalk/

Primary Focus:
Vision-seeking, dream navigation, storm invocation.

Modules:
	•	dreamwalk/weather.ms
	•	dreamwalk/navigation.ms
	•	dreamwalk/dream.ms

Primitives:
	•	weather.shift()
	•	dreamwalk.enter()
	•	storm.invoke()

⸻

L) South American Icaros & Plant Intelligence → std/icaros/

Primary Focus:
Ayahuasca icaro, kené pattern encoding, khipu topology.

Modules:
	•	icaros/song.ms
	•	icaros/kene.ms
	•	icaros/khipu.ms

Primitives:
	•	icaro.cast()
	•	kene.weave()
	•	khipu.knot()

⸻

M) Persian Magi / Zoroastrian Tradition → std/magi/

Primary Focus:
Sacred fire, duality engine, cosmic alignment.

Modules:
	•	magi/fire.ms
	•	magi/duality.ms

Primitives:
	•	fire.invoke()
	•	duality.balance()

⸻

N) Mesoamerican Calendrical & Jaguar Lore → std/nahualli/

Primary Focus:
Calendar cycles, sacrificial time logic, nahualli transformations.

Modules:
	•	nahualli/calendar.ms
	•	nahualli/shape.ms

Primitives:
	•	time.cycle()
	•	jaguar.shift()

⸻

O) Austronesian Mediumship & Spirit-Path → std/spiritpath/

Primary Focus:
Mediumship, trance-channeling, anti-colonial ritual innovation.

Modules:
	•	spiritpath/channel.ms
	•	spiritpath/induction.ms

Primitives:
	•	channel.open()
	•	spirit.enter()

⸻

P) Atlantic Resistance / Obeah / Revolt Magic → std/rebellion/

Primary Focus:
Obeah invocation, war-medicine, revolutionary spellwork.

Modules:
	•	rebellion/obeah.ms
	•	rebellion/war_spell.ms

Primitives:
	•	obeah.cast()
	•	warshield.raise()

⸻

3. Reverse Mapping — Primitive → Module → Lineage

This section helps developers quickly identify where a primitive originates.

Primitive	Module	Lineage Category
seal(...)	hermetic/seal.ms	Hermetic
angelic.call()	hermetic/enochian.ms	Hermetic
galdr.sing()	runes/galdr.ms	Nordic
psi.emit()	psychic/remote_influence.ms	Slavic
ancestor.call()	shamanic/ancestor.ms	Turkic/Anatolian
heka.formula()	heka/funeral_rites.ms	Egyptian
name.permute()	kabbalah/gematria.ms	Kabbalistic
djinn.bind()	djinn/binding.ms	Arab/Islamic
chant("OM")	mantra/chant.ms	Vedic
fu.draw()	onmyoji/fu.ms	East Asian
loa.mount()	vodun/loa.ms	African
fate.twist()	runes/elder_futhark.ms	Nordic
weather.shift()	dreamwalk/weather.ms	N. America / Polynesia
icaro.cast()	icaros/song.ms	S. America
fire.invoke()	magi/fire.ms	Persian
time.cycle()	nahualli/calendar.ms	Mesoamerican
channel.open()	spiritpath/channel.ms	Austronesian
obeah.cast()	rebellion/obeah.ms	Atlantic


⸻

4. Conclusion

This ontology establishes the complete symbolic → computational mapping of MPL.
It defines how cultural ritual systems are transformed into:
	•	Namespaces
	•	Standard libraries
	•	Primitives
	•	Semantic accents

This file is a core pillar of MPL’s theoretical and technical foundation.

⸻
