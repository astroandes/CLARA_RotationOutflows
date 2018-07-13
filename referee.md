Major comments:

1/ A strong divergence in the interpretation of the results:
Since rotation has been observed in any kind of astrophysical object, studying
the impact of rotation on Lya properties in the context of realistic galaxy
conditions is very worth!

And the authors achieve nice new results, for the first time: their study
nicely demonstrates that rotation does not have a strong impact on the global
shaping of the lya emission from galaxies.

Even in case of rapid rotation (Vrot = 100 km/s), the global shape of the
profile is still set by the radial velocity field (double peaks if static,
single red peak if outflow), while optical thickness is setting the scale of
the alteration (i.e. the amount of shift and broadening of the peaks).

Rotation has subtle effects, at least for the range of parameters investigated
here (see major comments 3 and 4), on the depth of the valley and the width of
the wings. 

To my knowledge, these are very interesting results which are
demonstrated here for the first time. They would have a strong impact on the
community if they were presented this way.

However, the authors are not clearly presenting them this way, still trying to
find probes of the impact of rotation on observed spectra (but see comments
below), which weakens the overall study.

[Jaime. Cambiar perspectiva.]

```diff
+ 2/ characterisation of the Lya profiles
```

I have a concern about the "quantitative results" shown in figs 2,3,4.
The authors characterise the lya line shapes by calculating the mean, standard
deviation, skewness, and bimodality of the distribution of emergent
frequencies. 
It is surprising, given the complexity of the shape of these
distributions. As well described in the text, it is then difficult to relate
the values of these estimates to any characteristics of the profile shapes, or
to any physical quantities. So is it really useful ?


For example, the standard deviation would trace the peak's location for a
double-peaked profile, whereas it would trace the width of the peak as soon as
the distribution becomes single-peaked... So interpreting what a standard
deviation of XXX km/s means is not straight-forward if we don't know Vout.

[Lo useful era para comparar con el modelo semianalico y para comparar rapidamente 
con muchos datos.]

Plus, these collections of 9 small windows are difficult to read and compare.
I suggest to try a single large plot instead of nine small ones, with
log(\tau_H) in abscisses and the measured quantity in y, and the different
values of Vrot and Vout coded by different symbols and colours.
For example, for Fig 2, this would better illustrate the fact that the
standard deviation, whatever it means, varies by a factor of ~2 when \tau_H
varies by one order of mag, whereas it varies by less than 10% when the
rotation goes from 0 to 100 km/s, and idem for the impact of outflow
velocities.

[Ya intentamos mostrarlo de esta manera. Dado que las escalas son diferentes
para cada valor de tau, es dificil seguir los trends en un plot unificado.
Ademas se complica la comparacion con el modelo seminalitico.]


3/ Thermal Velocity
There is an important parameter of your models that is not discussed: the
effect of varying the thermal velocity vth. Which thermal velocity do you
consider in this study ? From what I understand it is fixed to a single value,
right ? 

[Maria Camila. Yes it is fixed to 10^4 K 12.86 km/s]

However, since it appears explicitly in the "smoothing" term of
equation (4), depending on the ratio between Vrot and Vth, the effect of
rotation could be drastically different. In fact, this is not the absolute
value fo Vrot which is important, but the ratio Vrot/Vth. You should
investigate the dependance of the emergent Lya spectra depending on vth, or
varying the ratio Vrot/Vth. 

[De nuevo, el objetivo principal es comparar simulacion con el modelo semianalitico.
En ambos casos el ratio vrot/vth es el mismo, pero estamos de acuerdo con que 
hacer ajustes a observaciones deberia tener explicitamente este parametro. 
Nota para nosotros: elaborar este punto en texto y tal vez incluir al menos
una grafica variando v_th en la comparacion con valores observacionales.]

4/ low optical thickness regimes

it may be interesting to investigate the regimes of low optical thickness,
\tau_H~4 or below (corresponding to media transparent to LyC radiation),
because that is where the agreement with the analytical solution is not good.
In this regime, only numerical simulations can help predicting/understanding
the shape of the Lya profiles. And I would imagine that it is also the regime
where rotation may have a strong effect, since photons are escaping from the
inside.

[Maria Camila. preparar esos resultados y comentarlos.]


5/ spectral resolution
The rotation broadens the peaks and increases the flux at line center.
Spectral resolution would have exactly the same effect on a lya profile. With
you study, you could quantify which spectral sampling+resolution is necessary
to make sure that the broadening that is observed is not due to a too low
spectral resolution.

[Maria Camila. Intentar correr un modelo simple para estimar esos valores]


6/ triple-peaked lya profiles as proof of rotation ?
The authors discuss that two lya triple-peaked spectra could be shaped by
rotation: Tol1214-277 and the Sunburst. Both have new, complementary
observations not easily compatible with rotation as the main driver for their
Lya shape.

** Tol1214-277
The very peculiar shape in the low resolution GHRS lyman-alpha spectrum of
Tol1214-277 was modelled by the authors with a rotating model (Forrero+18).
However, it has been recently re-observed with COS, and shows a normal
double-peaked spectrum finally, as was shown by Goran Ostlin in the conference
in Tokyo last month:
http://www.icrr.u-tokyo.ac.jp/~toshijun/SakuraCLAW/slides/ostlin_CLAW.pdf

The weird triple-peak in the GHRS spectrum was probably due to low spectral
resolution and poor S/N. The valley in the higher spectral resolution, higher
signal to noise, spectrum goes to zero.
Rotation may not be necessary anymore to explain this kind of profile,
although the broad wings are not well reproduced by expanding shell models,
maybe better by clumpy outflows, as shown in the slides from Ostlin.

[Jaime: Reescribir para decir que no es necesario.]

** the Sunburst Arc
This is the only other triple peak even reported in the literature, as far as
I am aware (Rivera-Thorsen+17). This profile was suggested as tracing LyC
escape by Rivera+17, and new observations have just been done with HST, it is
nicely detected in LyC emission. I saw the data from a colleague of mine, they
will be published soon. So for this object either, rotation may not be the
main driver of the weird Lya shape.

[Jaime: Revisar esto.]

minor comments:

Abstract:
What are the physical arguments for the range of the parameters that you chose
? Which kind of galaxies are you thinking of ?
In particular, the rotational velocities seem on the high end of what is
observed, or correspond to massive objects, which are usually not strong Lya
emitters.
On the other hand, outflow velocities are rather low compared to the observed
velocities from absorption lines studies. 
I understand that it corresponds to cases where the effect of rotation is
expected to be maximal, but it would be useful to comment on these values, to
put them into context.

[Jaime: Reescribir el calculo y justificacion de los estimados]


Intro:
In the introduction, the authors try to motivate why it is important to study
Lya radiation transfer in rotating systems. I think it is very important, but
I don't find the argumentation convincing so far.
To my knowledge, there is a single study so far investigating a possible link
between the escape of Lya radiation from galaxies and their kinematics, from
the LARS team (Herenz+16).
They report that Lya is escaping preferentially from systems which are
dispersion dominated, so it seems that rotation does not help to be a strong
LAE, although their sample is quite small (~12 galaxies).
And the same with mass: low mass galaxies may not be often seen in rotation.
Although big spiral galaxies of the local Universe are nicely rotating, the
point of view that is presented in the introduction, i.e. the fact that
compact dwarf galaxies are rotationally supported, is not main stream.
Actually, in the cited study from Cairos+15, 4 out of 8 galaxies show no sign
of rotation: they have very irregular velocity maps. There are other IFU
studies of 4 "green peas"-like galaxies, called 'super compact UV bright
galaxies', from Basu-Zych+09, and 19 LBAs from GonÃ§alves+10, where they
report mainly perturbed, irregular kinematics.
Finally, recent studies at high redshift also report a low fraction of disks
at low mass, e.g. 25% only for Girard+18.
From my point of view, Lya emitters are usually low mass, and they are also
usually dispersion dominated systems.
Studying the effect of rotation on Lya radiation transfer is an interesting
study, however, he argumentation in the introduction is not very convincing so
far. I would suggest to find another angle, or to be more careful in the
statements: e.g. although most LAEs may not be rotation dominated systems,
rotation is a generic effect of gravitation. Idealised models with more and
more complicated geometries are investigated, but they all neglect rotation:
there is a severe lack of studies of the effect of rotation on the shape of
the Lya lines... etc....

[Jaime. Reescribir la argumentacion de la introdccion.]

first paragraph, ligne 8:
these systems naturally show a Lya emission line -> say 'produce' instead of
'show', since not all the star-forming galaxies with neutral gas and low dust
content show Lya in emission, whereas they produce a lot (not IZwicky18 for
example).

[Jaime]

4th paragraph, last sentence:
the citation of Yamada+12 is irrelevant here, since these are observations,
not radiation transfer studies.

[Jaime]

Theoretical Models:
Once again, the choice of the range of outflowing velocities is surprisingly
low (Vout = 0,25,50 km/s) compared to the several 100s of km/s usually
measured from absorption
line studies (e.g. Henry+15, Alexandroff+15, Chisholm+15,16,17,
Rivera-Thorsen+17). 
On the other hand, the rotation velocities are high compared to values
measured typically in IFU/IFS observations (Cairos+15, Basu-Zych+09).

[Jaime]

Results:
see the major comments below.
Discussion:
4.2 spatial variation of the profile on Fig6:
The authors make a nice prediction for a spatial variation of the lya profile
emerging from a rotating cloud, which is a strong prediction of their model,
and may be observable with MUSE or other IFU in the near future, but which
spectral resolution would be necessary to distinguish between the red side and
blue side spectra ?
About lya kinematic maps, the authors cite observational studies of Lya blobs
(Prescott+15, Arrigoni+18) which may be of different nature than the lya halos
observed around "normal" galaxies with MUSE (Wisotzki+16, Leclercq+17). In
particular, Patricio+16 show a lya kinematic map of the Lya halo of a lensed
galaxy observed with MUSE, and find no spatial variation of the lya profiles,
but the spectral resolution of MUSE may not be sufficient to see the predicted
effect.

[Jaime]

4.3 comparison with MUSE-Wide:
I am not sure to understand Fig7, why do you find that ~half of the sample has
a positive skewness ?!

[It's noisy and this is what we get]

Once again, this is not straightforward to understand the meaning of these
quantities for complicated and very inhomogeneous distributions as lya spectra
are, but you say in the text that a positive skewness is due to spectra with a
prominent blue peak. The MUSE-Wide LAE sample does NOT have half of the lya
spectra blue shifted. can you check/explain how you derived this quantity on
the observed spectra ? 

[Jaime]


COLORS: 
```diff
+ green: 
```
to reply to the referee

```diff
- red:
```
fixed in paper
