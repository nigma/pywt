/* Copyright (c) 2006-2012 Filip Wasilewski <http://en.ig.ma/> */
/* See COPYING for license details. */

/* Wavelet struct */

#ifndef _WAVELETS_H_
#define _WAVELETS_H_

#include "common.h"

/* Wavelet symmetry properties */
typedef enum {
    UNKNOWN = -1,
    ASYMMETRIC = 0,
    NEAR_SYMMETRIC = 1,
    SYMMETRIC = 2
} SYMMETRY;


/* Wavelet structure holding pointers to filter arrays and property attributes */
typedef struct {
        double* dec_hi_double;  /* highpass decomposition */
        double* dec_lo_double;  /* lowpass decomposition */
        double* rec_hi_double;  /* highpass reconstruction */
        double* rec_lo_double;  /* lowpass reconstruction */
        float* dec_hi_float;
        float* dec_lo_float;
        float* rec_hi_float;
        float* rec_lo_float;
    
    index_t dec_len;   /* length of decomposition filter */
    index_t rec_len;   /* length of reconstruction filter */
    
    /* Wavelet properties */
    int vanishing_moments_psi;
    int vanishing_moments_phi;
    index_t support_width;

    SYMMETRY symmetry;

    int orthogonal:1;
    int biorthogonal:1;
    int compact_support:1;

    /*
     * Set if filters arrays shouldn't be deallocated by
     * free_wavelet(Wavelet) func
     */
    int _builtin:1;

    char* family_name;
    char* short_name;

} Wavelet;


/* 
 * Allocate Wavelet struct and set its attributes
 * name - (currently) a character codename of a wavelet family
 * order - order of the wavelet (ie. coif3 has order 3)
 *
 * _builtin field is set to 1
 */
Wavelet* wavelet(char name, int order);

/* 
 * Allocate blank Wavelet with zero-filled filters of given length
 * _builtin field is set to 0
 */
Wavelet* blank_wavelet(index_t filters_length);

/* Deep copy Wavelet */
Wavelet* copy_wavelet(Wavelet* base);

/* 
 * Free wavelet struct. Use this to free Wavelet allocated with
 * wavelet(...) or blank_wavelet(...) functions.
 */
void free_wavelet(Wavelet *wavelet);

#endif
