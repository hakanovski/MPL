ONTOLOGY

Magus Lineages → MPL Standard Library Mapping (v1.0)

This document defines how the 225 historical magus lineages from MANIFESTO.md map into MPL’s standard library, namespaces, primitives, and semantic structure.

Each lineage acts as a cultural “accent module” contributing unique symbolic and computational patterns.

⸻

1. Ontology Structure

For each cultural lineage:
	•	Primary Focus
	•	Mapped stdlib modules
	•	Canonical primitives introduced
	•	Symbolic influence on syntax

Module path format:

stdlib/<namespace>/<module>.ms

Primitive format:

namespace.operation()


⸻

2. Cultural Lineages → Standard Library Mapping

⸻

A) The Hermetic Core → std/hermetic/

Primary Focus:
Sigils, planetary correspondences, ceremonial magic, alchemy, Enochian syntax.

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
Telepathy, remote influence, bio-energy projection.

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
Ancestor work, nature spirits, dream-walking.

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
Death rites, heka formulas, preservation magic.

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
Gematria, divine names, textual permutation logic.

Modules:
	•	kabbalah/gematria.ms
	•	kabbalah/names.ms

Primitives:
	•	name.permute()
	•	golem.construct()
	•	sefirot.map()

⸻

F) Arab / Islamic Occult Tradition → std/djinn/

Primary Focus:
Talismanic diagrams, djinn-binding, abjad numerology.

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
Mantras, yantras, prana-routing, siddhi logic.

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
Shikigami, talismans (fu), element-routing.

Modules:
	•	onmyoji/shikigami.ms
	•	onmyoji/fu.ms
	•	onmyoji/elements.ms

Primitives:
	•	fu.draw()
	•	shikigami.call()
	•	element.route()

⸻

I) African Vodun / Fetish / Ancestor Traditions → std/vodun/

Primary Focus:
Possession, loa mounting, fetish engineering.

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
Rune carving, galdr (chant magic), fate manipulation.

Modules:
	•	runes/elder_futhark.ms
	•	runes/galdr.ms

Primitives:
	•	rune.carve()
	•	galdr.sing()
	•	fate.twist()

⸻

K) Native American / Polynesian Dream & Weather → std/dreamwalk/

Primary Focus:
Dreamwalking, storm invocation, spirit-navigation.

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
Ayahuasca icaro, kené pattern encoding, khipu knot structures.

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
Sacred fire, duality physics, cosmic alignment.

Modules:
	•	magi/fire.ms
	•	magi/duality.ms

Primitives:
	•	fire.invoke()
	•	duality.balance()

⸻

N) Mesoamerican Calendrical & Jaguar Lore → std/nahualli/

Primary Focus:
Calendar cycles, sacrificial time, nahualli transformation.

Modules:
	•	nahualli/calendar.ms
	•	nahualli/shape.ms

Primitives:
	•	time.cycle()
	•	jaguar.shift()

⸻

O) Austronesian Mediumship → std/spiritpath/

Primary Focus:
Mediumship, trance-channeling, ancestral pathways.

Modules:
	•	spiritpath/channel.ms
	•	spiritpath/induction.ms

Primitives:
	•	channel.open()
	•	spirit.enter()

⸻

P) Atlantic Resistance / Obeah / War-Medicine → std/rebellion/

Primary Focus:
Revolution magic, war-shields, Obeah invocation.

Modules:
	•	rebellion/obeah.ms
	•	rebellion/war_spell.ms

Primitives:
	•	obeah.cast()
	•	warshield.raise()

⸻

**3. Reverse Mapping

Primitive → Module → Lineage**

Primitive	Module	Lineage
seal(...)	hermetic/seal.ms	Hermetic
angelic.call()	hermetic/enochian.ms	Hermetic
sigil.draw()	hermetic/seal.ms	Hermetic
psi.emit()	psychic/remote_influence.ms	Slavic/Russian
ancestor.call()	shamanic/ancestor.ms	Turkic/Anatolian
wind.invoke()	shamanic/nature_spirit.ms	Turkic/Anatolian
dream.enter()	shamanic/dreampath.ms	Turkic/Anatolian
heka.formula()	heka/funeral_rites.ms	Egyptian
ka.bind()	heka/preservation.ms	Egyptian
name.permute()	kabbalah/gematria.ms	Kabbalistic
golem.construct()	kabbalah/names.ms	Kabbalistic
djinn.bind()	djinn/binding.ms	Arab/Islamic
talisman.draw()	djinn/talisman.ms	Arab/Islamic
chant("OM")	mantra/chant.ms	Vedic/Himalayan
yantra.draw()	mantra/yantra.ms	Vedic/Himalayan
fu.draw()	onmyoji/fu.ms	East Asian
shikigami.call()	onmyoji/shikigami.ms	East Asian
loa.mount()	vodun/loa.ms	African
ashe.flow()	vodun/inkisi.ms	African
rune.carve()	runes/elder_futhark.ms	Nordic
galdr.sing()	runes/galdr.ms	Nordic
weather.shift()	dreamwalk/weather.ms	N. America / Polynesia
dreamwalk.enter()	dreamwalk/dream.ms	N. America / Polynesia
icaro.cast()	icaros/song.ms	S. America
khipu.knot()	icaros/khipu.ms	S. America
fire.invoke()	magi/fire.ms	Persian
duality.balance()	magi/duality.ms	Persian
time.cycle()	nahualli/calendar.ms	Mesoamerican
jaguar.shift()	nahualli/shape.ms	Mesoamerican
channel.open()	spiritpath/channel.ms	Austronesian
spirit.enter()	spiritpath/induction.ms	Austronesian
obeah.cast()	rebellion/obeah.ms	Atlantic
warshield.raise()	rebellion/war_spell.ms	Atlantic


⸻

4. Conclusion

This ontology defines the structural relationship between:
	•	Cultural lineage
	•	Ritual pattern
	•	Namespace
	•	Standard Library module
	•	Primitive function

It is a core, foundational document for MPL’s symbolic runtime and semantic identity.

⸻

