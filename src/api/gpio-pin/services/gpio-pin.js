'use strict';

/**
 * gpio-pin service
 */

const { createCoreService } = require('@strapi/strapi').factories;

module.exports = createCoreService('api::gpio-pin.gpio-pin');
