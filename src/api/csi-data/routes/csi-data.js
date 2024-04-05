'use strict';

/**
 * csi-data router
 */

const { createCoreRouter } = require('@strapi/strapi').factories;

module.exports = createCoreRouter('api::csi-data.csi-data');
