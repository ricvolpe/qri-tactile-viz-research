<summary>Table of Contents</summary>
<ol>
<li>
    <a href="#experiment-1-single-sine-waves">
        Experiment 1
    </a>
</li>
<li>
    <a href="#experiment-2-pairs-of-sine-waves">
        Experiment 2
    </a>
</li>
<li>
    <a href="#experiment-3-frequency-symmetry-and-emotions">
        Experiment 3
    </a>
</li>
<li>
    <a href="#user-data">
        User data
    </a>
</li>
</ol>

## Experiment 1: single sine waves
Experiment 1 used *stimuli v1* which consisted of 
* a full body silhouette
* low amplitude waves with lots of black space in between
* sinusoidal waves with 
    * temporal waveform roughly varying exponentially between 1 and 16 Hz
    * spatial waveform roughly varying linearly between 4 and 10 vertical bands

[`e1_sine_waves_questions.csv`](e1_sine_waves_questions.csv) has the data about the parametrised versions of stimuli v1 used for each survey question, more specifically
* `question_id` can be used to map to survey responses
* `spatial_waveform` describes the spatial heigth of the sinousoudal waves. A value of 20 roughly corresponds to 4 vertical bands while a value of 10 roughly corresponds to 10.
* `temporal_waveform` describes the temporal flickering of the waves and it roughly corresponds to Hz
* `stimuli_video` has the YouTube link for each specific stimuli.

The YouTube playlist of all the stimuli used in experiment 1 is https://youtube.com/playlist?list=PLJSFo5kq-dxpEnTDEPQK_Px8Du53nO42z

The code for stimuli v1 can be found in this shader: https://www.shadertoy.com/view/ctScWm

[`e1_sine_waves_items.csv`](e1_sine_waves_items.csv) has the data about the participants responses to a survey that showed the variations of stimuli v1 and asked the following questions
* How **pleasant** do you feel this sensation is?
* How **intense** do you feel this sensation is?
* How **stimulating** do you feel this sensation is?
* How **complex** do you feel this sensation is?

All responses were collected as Likert scales ranging from 1 (not at all) to 10 (very pleasant/intense/stimulating/complex).

## Experiment 2: pairs of sine waves
In experiment 2, we displayed superimposed pairs of sinusoidal waves. We ran two different versions of experiment 2, one using relatively fast and small waveforms (experiment 2a, stimuli v1) and one using relatively slower and wider waveforms (experiment 2b, stimuli v2).

### Experiment 2a
Experiment 2a used *stimuli v1*, the same as in [experiment 1](#experiment-1-single-sine-waves). 

We created pairs of waves by superimposing
* one baseline wave (roughly 4Hz and 4 bands)
* a second wave chosen by changing either the temporal or the spatial waveform

[`e2a_sine_waves_pairs_questions.csv`](e2a_sine_waves_pairs_questions.csv) has the data about the parametrised versions of stimuli v1 used for each survey question, where the data columns have the same meaning as in [experiment 1](#experiment-1-single-sine-waves) except for the fact that now we have two spatial and temporal waveform values.

The YouTube playlist of all the stimuli used in experiment 2a is: https://youtube.com/playlist?list=PLJSFo5kq-dxrykAAq_59IloTV-hvKw3c2

The shader code is the same as the one used for experiment 1: https://www.shadertoy.com/view/ctScWm

### Experiment 2b
Experiment 2b used a different stimuli (*stimuli v2*), consisting of
* a silhouette of the upper half of body
* high amplitude waves forming whole thorax blobs
superimposed pairs of sinusoidal waves with
    * temporal waveform roughly varying linearly between 2 and 4 Hz
    * spatial waveform roughly varying linearly between 1 and 4 vertical bands
* the same logic for creating superimposed waves as in [experiment 2a](#experiment-2a)

In experiment 2b, we collected impressions of spatial and temporal waveform variations separately. Besides that, Experiment 2b data follow the same structure of [experiment 1](#experiment-1-single-sine-waves) and [experiment 2a](#experiment-2a).

The code for stimuli v2 can be found in this shader: https://www.shadertoy.com/view/ddyfRR 

Fully Youtube playlist of ttimuli for experiment 2b can be seen here:
* temporal: https://youtube.com/playlist?list=PLJSFo5kq-dxq7HD7IjKiq9rQMoxR-2_CJ
* spatial: https://youtube.com/playlist?list=PLJSFo5kq-dxrZWlXJu9pigKAbGnxDb8Y9

## Experiment 3: frequency, symmetry and emotions

In experiment 3 we created four different stimuli aiming to depict four different emotional states: anxiety, depression, serenity and excitement.

The stimuli are combinations of low-high frequency and low-high symmetry of sinusoidal waves over a body silhouette and can be seen here:
* excitement: https://www.youtube.com/watch?v=rfpZ_cUobp4
* anxiety: https://www.youtube.com/watch?v=prpqTWKotbY
* serenity: https://www.youtube.com/watch?v=0rvqtGBrOAI
* depression: https://www.youtube.com/watch?v=67OvWwnZSjU

We showed the four stimuli to 50 survey participants, invited them to try embody them and asked the following questions
* is this visualization **easy to embody**?
* is this visualization **pleasant**?
* is this visualization **simulating**?
* Which emotion best describes how your body feels when you embody this visualization?

Responses to the first three question were collected as Likert scales ranging from 1 (not at all) to 5 (very embody/pleasant/stimulating).

[`e3_emotions.csv`](e3_emotions.csv) contains the resulting data where
* *embody/valence/arousal* describe the user answer to the above Likert-scale questions
* *emotion* describes the emotion chosen by respondent
* *depiction* describes the emotion we tried to depict and showed to the respondent

## User data

For all experiments 1 and 2 we also collected user data such as
* height
* an open ended question asking if there was anything unclear in the experiment (`anything_unclear`)
* an open ended question asking if there was anthing else they wanted to tell us (`other_comments`)

These data are available in all the files ending with `_users.csv`. We have not used any of them in our analysis.