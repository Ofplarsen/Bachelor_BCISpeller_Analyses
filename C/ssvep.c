#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <SDL2/SDL.h>

int main(int argc, char *argv[]) {
        if (argc != 2) {
        printf("Usage: %s <frequency>\n", argv[0]);
        return 1;
    }

    int frequency = atoi(argv[1]);
    if (frequency <= 0) {
        printf("Invalid frequency. Please provide a positive integer value.\n");
        return 1;
    }
    if (SDL_Init(SDL_INIT_VIDEO) < 0) {
        printf("SDL could not initialize! SDL_Error: %s\n", SDL_GetError());
        return 1;
    }

    SDL_Window *window = SDL_CreateWindow("Flicker",
                                          SDL_WINDOWPOS_CENTERED,
                                          SDL_WINDOWPOS_CENTERED,
                                          800, 600,
                                          SDL_WINDOW_SHOWN);
    if (window == NULL) {
        printf("Window could not be created! SDL_Error: %s\n", SDL_GetError());
        SDL_Quit();
        return 1;
    }

    SDL_Renderer *renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED);
    if (renderer == NULL) {
        printf("Renderer could not be created! SDL_Error: %s\n", SDL_GetError());
        SDL_DestroyWindow(window);
        SDL_Quit();
        return 1;
    }

    
    Uint32 interval = (Uint32)(1000.0 / (2.0 * frequency));

    bool quit = false;
    bool white = false;
    SDL_Event event;
    Uint32 next_flicker = SDL_GetTicks() + interval;

    while (!quit) {
        while (SDL_PollEvent(&event)) {
            if (event.type == SDL_QUIT) {
                quit = true;
            }
        }

        if (SDL_GetTicks() >= next_flicker) {
            white = !white;
            next_flicker += interval;
        }

        SDL_SetRenderDrawColor(renderer, white ? 255 : 0, white ? 255 : 0, white ? 255 : 0, 255);
        SDL_RenderClear(renderer);
        SDL_RenderPresent(renderer);
    }

    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(window);
    SDL_Quit();
    return 0;
}

