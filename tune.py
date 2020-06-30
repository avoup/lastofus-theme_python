from wave import open
from struct import Struct
from math import floor

frame_rate = 11025

def encode(x):
    i = int(16384 * x)
    return Struct('h').pack(i)

def play(sampler, name='tune.wav', seconds = 2):
    out = open(name, 'wb')

    out.setnchannels(1)
    out.setsampwidth(2)
    out.setframerate(frame_rate)

    f = 0
    while f < seconds * frame_rate:
        sample = sampler(f)
        out.writeframes(encode(sample))
        f += 1

    out.close()

def tri(freq, amp=0.3):
    p = frame_rate // freq

    def sampler(t):
        saw_wave = t / p - floor( t/p + 0.5)
        tri_wave = 2 * abs(2 * saw_wave) - 1
        return tri_wave * amp
    return sampler


freq_c = 16.35
freq_c_sharp = 17.32
freq_d = 18.35
freq_d_sharp = 19.45
freq_e = 20.60
freq_f = 21.83
freq_f_sharp = 23.12
freq_g = 24.50
freq_g_sharp = 25.96
freq_a = 27.50
freq_a_sharp = 29.14
freq_b = 30.87



def tune(freq, octave=4):
    assert freq < 31, 'freq should be less than 31'
    assert freq > 0, 'freq should be more than 0'

    if octave == 0:
        return freq
    return tune(freq, octave -1) * 2

def dyad(a, b):
    return lambda t: a(t) + b(t)


def note(n, start, end, fade_in=0.01, fade_out=0.1):
    def sampler(t):
        seconds = t / frame_rate

        if seconds < start:
            return 0
        elif seconds > end:
            return 0
        elif seconds < start + fade_in:
            return (seconds - start) / fade_in * n(t)
        elif seconds > end - fade_out:
            return (end - seconds) / fade_out * n(t)
        else:
            return n(t)
    return sampler

def chord(freq, octave=4):
    return tri(tune(freq, octave))

c4 = chord(freq_c, 4)
b4 = chord(freq_b, 4)
b3 = chord(freq_b, 3)
g4 = chord(freq_g, 4)
e4 = chord(freq_e, 4)
a4 = chord(freq_a, 4)
f4 = chord(freq_f, 4)
a4_sharp = chord(freq_a_sharp, 4)
g3 = chord(freq_g, 3)

# ( g4, b3, e4 ) x 4 
# e4 b3 e4
# a4 b3 e4
# f4 b3 e4
# ( g4 b3 e4 ) x3


def melody():
    t = 1/4.5
    tt = 1/6

    z = 0 #initialize z at 0
    song = note(g4, z, z + t)
    z+= tt
    song = dyad(song, note(b3, z, z + t))
    z += tt
    song = dyad(song, note(e4, z, z + t))
    z += tt

    song = dyad(song, note(g4, z, z + t))
    z += tt
    song = dyad(song, note(b3, z, z + t))
    z += tt
    song = dyad(song, note(e4, z, z + t))
    z += tt

    song = dyad(song, note(g4, z, z + t))
    z += tt
    song = dyad(song, note(b3, z, z + t))
    z += tt
    song = dyad(song, note(e4, z, z + t))
    z += tt

    song = dyad(song, note(g4, z, z + t))
    z += tt
    song = dyad(song, note(b3, z, z + t))
    z += tt
    song = dyad(song, note(e4, z, z + t))
    z += tt

    song = dyad(song, note(e4, z, z + t))
    z += tt
    song = dyad(song, note(b3, z, z + t))
    z += tt
    song = dyad(song, note(e4, z, z + t))
    z += tt

    song = dyad(song, note(a4, z, z + t))
    z += tt
    song = dyad(song, note(b3, z, z + t))
    z += tt
    song = dyad(song, note(e4, z, z + t))
    z += tt

    song = dyad(song, note(f4, z, z + t))
    z += tt
    song = dyad(song, note(b3, z, z + t))
    z += tt
    song = dyad(song, note(e4, z, z + t))
    z += tt

    song = dyad(song, note(g4, z, z + t))
    z += tt
    song = dyad(song, note(b3, z, z + t))
    z += tt
    song = dyad(song, note(e4, z, z + t))
    z += tt

    song = dyad(song, note(g4, z, z + t))
    z += tt
    song = dyad(song, note(b3, z, z + t))
    z += tt
    song = dyad(song, note(e4, z, z + t))
    z += tt

    song = dyad(song, note(g4, z, z + t))
    z += tt
    song = dyad(song, note(b3, z, z + t))
    z += tt
    song = dyad(song, note(e4, z, z + t))
    z += tt

    song = dyad(song, note(e4, z, z + t))
    z += tt
    song = dyad(song, note(b3, z, z + t))
    z += tt
    song = dyad(song, note(e4, z, z + t))
    z += tt

    song = dyad(song, note(a4, z, z + t))
    z += tt
    song = dyad(song, note(b3, z, z + t))
    z += tt
    song = dyad(song, note(e4, z, z + t))
    z += tt

    song = dyad(song, note(f4, z, z + t))
    z += tt
    song = dyad(song, note(b3, z, z + t))
    z += tt
    song = dyad(song, note(e4, z, z + t))
    z += tt

    song = dyad(song, note(b4, z, z + t))
    z += tt
    song = dyad(song, note(b3, z, z + t))
    z += tt
    song = dyad(song, note(e4, z, z + t))
    z += tt

    song = dyad(song, note(b4, z, z + t))
    z += tt
    song = dyad(song, note(b3, z, z + t))
    z += tt
    song = dyad(song, note(e4, z, z + t))
    z += tt

    song = dyad(song, note(b4, z, z + t))
    z += tt
    song = dyad(song, note(b3, z, z + t))
    z += tt
    song = dyad(song, note(e4, z, z + t))
    z += tt

    song = dyad(song, note(b4, z, z + t))
    z += tt
    song = dyad(song, note(b3, z, z + t))
    z += tt
    song = dyad(song, note(e4, z, z + t))
    z += tt

    song = dyad(song, note(g4, z, z + t))
    z += tt
    song = dyad(song, note(b3, z, z + t))
    z += tt
    song = dyad(song, note(e4, z, z + t))
    z += tt

    song = dyad(song, note(e4, z, z + t))
    z += tt
    song = dyad(song, note(b3, z, z + t))
    z += tt
    song = dyad(song, note(e4, z, z + t))
    z += tt

    song = dyad(song, note(a4, z, z + t))
    z += tt
    song = dyad(song, note(b3, z, z + t))
    z += tt
    song = dyad(song, note(e4, z, z + t))
    z += tt

    song = dyad(song, note(f4, z, z + t))
    z += tt
    song = dyad(song, note(b3, z, z + t))
    z += tt
    song = dyad(song, note(e4, z, z + t))
    z += tt

    song = dyad(song, note(g4, z, z + t))
    z += tt
    song = dyad(song, note(b3, z, z + t))
    z += tt
    song = dyad(song, note(e4, z, z + t))
    z += tt

    song = dyad(song, note(g4, z, z + t))
    z += tt
    song = dyad(song, note(b3, z, z + t))
    z += tt
    song = dyad(song, note(e4, z, z + t))
    z += tt

    song = dyad(song, note(g4, z, z + t))
    z += tt
    song = dyad(song, note(b3, z, z + t))
    z += tt
    song = dyad(song, note(e4, z, z + t))
    z += tt

    song = dyad(song, note(g4, z, z + t))
    z += tt
    song = dyad(song, note(b3, z, z + t))
    z += tt
    song = dyad(song, note(e4, z, z + t))
    z += tt

    song = dyad(song, note(a4_sharp, z, z + t))
    z += tt
    song = dyad(song, note(b3, z, z + t))
    z += tt
    song = dyad(song, note(e4, z, z + t))
    z += tt

    song = dyad(song, note(a4, z, z + t))
    z += tt
    song = dyad(song, note(b3, z, z + t))
    z += tt
    song = dyad(song, note(e4, z, z + t))
    z += tt

    song = dyad(song, note(g4, z, z + t))
    z += tt
    song = dyad(song, note(b3, z, z + t))
    z += tt
    song = dyad(song, note(e4, z, z + t))
    z += tt

    song = dyad(song, note(e4, z, z + t))
    z += tt
    song = dyad(song, note(b3, z, z + t))
    z += tt
    song = dyad(song, note(e4, z, z + t))
    z += tt

    song = dyad(song, note(g4, z, z + t))
    z += tt
    song = dyad(song, note(g3, z, z + t))
    z += tt
    song = dyad(song, note(b3, z, z + t))
    z += tt

    song = dyad(song, note(g4, z, z + t))
    z += tt
    song = dyad(song, note(g3, z, z + t))
    z += tt
    song = dyad(song, note(b3, z, z + t))
    z += tt

    song = dyad(song, note(g4, z, z + t))
    z += tt
    song = dyad(song, note(g3, z, z + t))
    z += tt
    song = dyad(song, note(b3, z, z + t))
    z += tt

    return song

play(melody(), 'lastofus.wav', 16)

