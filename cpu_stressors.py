import asyncio
import itertools
import math


async def loop2():
    try:
        x = 0
        for _ in itertools.count():
            x += 1
            await asyncio.sleep(0)
    except asyncio.CancelledError as ex:
        print (f"{x} iterations")
        raise ex



async def euler():
    try:
        e = 0
        n = 0
        while True:
            term = 1 / math.factorial(n)
            e += term
            n += 1
            await asyncio.sleep(0)
    except asyncio.CancelledError as ex:
        print(f"e = {e}")
        raise ex

async def euler2():
    e = 0
    n = 0
    while True:
        term = 1 / math.factorial(n)
        e += term
        n += 1
        await asyncio.sleep(0)





    #    --cpu-method method
    #           specify a cpu stress method. By default,  all  the  stress  methods  are  exercised
    #           sequentially,  however  one  can  specify  just  one method to be used if required.
    #           Available cpu stress methods are described as follows:

    #           Method           Description
    #           all              iterate over all the below cpu stress methods
    #           ackermann        Ackermann function: compute A(3, 10), where:
    #                             A(m, n) = n + 1 if m = 0;
    #                             A(m - 1, 1) if m > 0 and n = 0;
    #                             A(m - 1, A(m, n - 1)) if m > 0 and n > 0
    #           bitops           various bit operations from bithack, namely: reverse bits,  parity
    #                            check, bit count, round to nearest power of 2
    #           callfunc         recursively  call  8  argument C function to a depth of 1024 calls
    #                            and unwind
    #           cfloat           1000 iterations of a mix of floating point complex operations
    #           cdouble          1000  iterations  of  a  mix  of  double  floating  point  complex
    #                            operations
    #           clongdouble      1000  iterations  of  a  mix of long double floating point complex
    #                            operations
    #           correlate        perform a 16384 × 1024 correlation of random doubles
    #           crc16            compute 1024 rounds of CCITT CRC16 on random data
    #           decimal32        1000 iterations  of  a  mix  of  32  bit  decimal  floating  point
    #                            operations (GCC only)
    #           decimal64        1000  iterations  of  a  mix  of  64  bit  decimal  floating point
    #                            operations (GCC only)
    #           decimal128       1000 iterations of  a  mix  of  128  bit  decimal  floating  point
    #                            operations (GCC only)
    #           dither           Floyd–Steinberg dithering of a 1024 × 768 random image from 8 bits
    #                            down to 1 bit of depth.
    #           djb2a            128 rounds of  hash  DJB2a  (Dan  Bernstein  hash  using  the  xor
    #                            variant) on 128 to 1 bytes of random strings
    #           double           1000  iterations  of  a  mix  of  double  precision floating point
    #                            operations
    #           euler            compute e using n = (1 + (1 ÷ n)) ↑ n
    #           explog           iterate on n = exp(log(n) ÷ 1.00002)
    #           fibonacci        compute Fibonacci sequence of 0, 1, 1, 2, 5, 8...
    #           fft              4096 sample Fast Fourier Transform
    #           float            1000 iterations of a mix of floating point operations
    #           fnv1a            128 rounds of hash FNV-1a (Fowler–Noll–Vo hash using the xor  then
    #                            multiply variant) on 128 to 1 bytes of random strings
    #           gamma            calculate  the  Euler-Mascheroni  constant  γ  using  the limiting
    #                            difference between the harmonic series (1 + 1/2 + 1/3 + 1/4 +  1/5
    #                            ... + 1/n) and the natural logarithm ln(n), for n = 80000.
    #           gcd              compute GCD of integers
    #           gray             calculate  binary  to  gray  code and gray code back to binary for
    #                            integers from 0 to 65535
    #           hamming          compute Hamming H(8,4) codes on 262144 lots of 4  bit  data.  This
    #                            turns 4 bit data into 8 bit Hamming code containing 4 parity bits.
    #                            For data bits d1..d4, parity bits are computed as:
    #                              p1 = d2 + d3 + d4
    #                              p2 = d1 + d3 + d4
    #                              p3 = d1 + d2 + d4
    #                              p4 = d1 + d2 + d3
    #           hanoi            solve a 21 disc Towers of Hanoi stack using the recursive solution
    #           hyperbolic       compute sinh(θ) × cosh(θ) + sinh(2θ) + cosh(3θ) for float,  double
    #                            and  long  double hyperbolic sine and cosine functions where θ = 0
    #                            to 2π in 1500 steps
    #           idct             8 × 8 IDCT (Inverse Discrete Cosine Transform)
    #           int8             1000 iterations of a mix of 8 bit integer operations
    #           int16            1000 iterations of a mix of 16 bit integer operations
    #           int32            1000 iterations of a mix of 32 bit integer operations
    #           int64            1000 iterations of a mix of 64 bit integer operations

    #           int128           1000 iterations of a mix of 128 bit integer operations (GCC only)
    #           int32float       1000 iterations of a mix of 32  bit  integer  and  floating  point
    #                            operations
    #           int32double      1000  iterations  of  a mix of 32 bit integer and double precision
    #                            floating point operations
    #           int32longdouble  1000 iterations of a  mix  of  32  bit  integer  and  long  double
    #                            precision floating point operations
    #           int64float       1000  iterations  of  a  mix  of 64 bit integer and floating point
    #                            operations
    #           int64double      1000 iterations of a mix of 64 bit integer  and  double  precision
    #                            floating point operations
    #           int64longdouble  1000  iterations  of  a  mix  of  64  bit  integer and long double
    #                            precision floating point operations
    #           int128float      1000 iterations of a mix of 128 bit  integer  and  floating  point
    #                            operations (GCC only)
    #           int128double     1000  iterations  of a mix of 128 bit integer and double precision
    #                            floating point operations (GCC only)
    #           int128longdouble 1000 iterations of a mix  of  128  bit  integer  and  long  double
    #                            precision floating point operations (GCC only)
    #           int128decimal32  1000  iterations  of  a  mix of 128 bit integer and 32 bit decimal
    #                            floating point operations (GCC only)
    #           int128decimal64  1000 iterations of a mix of 128 bit integer  and  64  bit  decimal
    #                            floating point operations (GCC only)
    #           int128decimal128 1000  iterations  of  a mix of 128 bit integer and 128 bit decimal
    #                            floating point operations (GCC only)
    #           jenkin           Jenkin's integer hash on 128 rounds of 128..1 bytes of random data
    #           jmp              Simple unoptimised compare >, <, == and jmp branching
    #           ln2              compute ln(2) based on series:
    #                             1 - 1/2 + 1/3 - 1/4 + 1/5 - 1/6 ...
    #           longdouble       1000 iterations of a mix of long double precision  floating  point
    #                            operations
    #           loop             simple empty loop
    #           matrixprod       matrix product of two 128 × 128 matrices of double floats. Testing
    #                            on 64 bit x86 hardware shows that this is provides a good  mix  of
    #                            memory,  cache  and  floating point operations and is probably the
    #                            best CPU method to use to make a CPU run hot.
    #           nsqrt            compute sqrt() of long doubles using Newton-Raphson
    #           omega            compute the omega constant defined by Ωe↑Ω  =  1  using  efficient
    #                            iteration of Ωn+1 = (1 + Ωn) / (1 + e↑Ωn)
    #           parity           compute  parity  using  various  methods  from  the  Standford Bit
    #                            Twiddling Hacks.  Methods employed are: the naïve way,  the  naïve
    #                            way  with  the  Brian  Kernigan  bit  counting  optimisation,  the
    #                            multiply way, the parallel way,  and  the  lookup  table  ways  (2
    #                            variations).
    #           phi              compute the Golden Ratio ϕ using series
    #           pi               compute π using the Srinivasa Ramanujan fast convergence algorithm
    #           pjw              128  rounds  of  hash  pjw  function  on  128 to 1 bytes of random
    #                            strings
    #           prime            find all the primes in the  range   1..1000000  using  a  slightly
    #                            optimised brute force naïve trial division search
    #           psi              compute ψ (the reciprocal Fibonacci constant) using the sum of the
    #                            reciprocals of the Fibonacci numbers
    #           queens           compute all the solutions of the  classic  8  queens  problem  for
    #                            board sizes 1..12
    #           rand             16384  iterations  of  rand(), where rand is the MWC pseudo random
    #                            number generator.  The MWC random function concatenates two 16 bit
    #                            multiply-with-carry generators:
    #                             x(n) = 36969 × x(n - 1) + carry,
    #                             y(n) = 18000 × y(n - 1) + carry mod 2 ↑ 16

    #                            and has period of around 2 ↑ 60
    #           rand48           16384 iterations of drand48(3) and lrand48(3)
    #           rgb              convert RGB to YUV and back to RGB (CCIR 601)
    #           sdbm             128 rounds of hash sdbm (as used in the SDBM database and GNU awk)
    #                            on 128 to 1 bytes of random strings
    #           sieve            find the primes in  the  range  1..10000000  using  the  sieve  of
    #                            Eratosthenes
    #           sqrt             compute  sqrt(rand()),  where rand is the MWC pseudo random number
    #                            generator

    #           trig             compute sin(θ) × cos(θ) + sin(2θ) + cos(3θ) for float, double  and
    #                            long  double  sine  and cosine functions where θ = 0 to 2π in 1500
    #                            steps
    #           union            perform integer arithmetic on a mix of bit fields in  a  C  union.
    #                            This  exercises  how well the compiler and CPU can perform integer
    #                            bit field loads and stores.
    #           zeta             compute the Riemann Zeta function ζ(s) for s = 2.0..10.0

    #           Note that some of these methods try to exercise the CPU with computations found  in
    #           some  real  world  use  cases.  However,  the code has not been optimised on a per-
    #           architecture basis, so may be a sub-optimal compared to hand-optimised code used in
    #           some applications.  They do try to represent the typical instruction mixes found in
    #           these use cases.